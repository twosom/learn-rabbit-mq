import rabbitpy
from rabbitpy import Queue

with rabbitpy.Connection() as conn:
    with conn.channel() as channel:
        queue: Queue = rabbitpy.Queue(channel, 'test-messages')
        queue.declare()
        while True:
            message = queue.get()
            if message:
                message.pprint()
                message.ack()
                if message.body == 'stop':
                    break
