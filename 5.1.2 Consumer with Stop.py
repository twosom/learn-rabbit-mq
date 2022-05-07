import rabbitpy
from rabbitpy import Channel, Message

with rabbitpy.Connection() as connection:
    channel: Channel
    with connection.channel() as channel:
        message: Message
        for message in rabbitpy.Queue(channel, 'test-messages'):
            message.pprint()
            message.ack()
            if message.body == 'stop':
                break
