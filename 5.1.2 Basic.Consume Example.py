import rabbitpy
from rabbitpy import Message

message: Message
for message in rabbitpy.consume('amqp://guest:guest@localhost:5672/%2f', 'test-messages'):
    message.pprint()
    message.ack()
