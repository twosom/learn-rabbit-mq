import rabbitpy
from rabbitpy import Channel, Queue

with rabbitpy.Connection() as connection:
    channel: Channel
    with connection.channel() as channel:
        queue: Queue = rabbitpy.Queue(channel, 'test-messages')
        for message in queue.consume(no_ack=True):
            message.pprint()
