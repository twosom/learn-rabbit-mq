import rabbitpy
from rabbitpy import Exchange, Channel, Message


def create_message():
    return rabbitpy.Message(channel, 'This is an important message',
                            {'content_type': 'text/plain',
                             'message_type': 'very important'})


with rabbitpy.Connection() as connection:
    channel: Channel
    with connection.channel() as channel:
        exchange: Exchange = rabbitpy.Exchange(channel, 'chapter4-example')
        exchange.declare()  # Exchange 선언
        channel.enable_publisher_confirms()  # RabbitMQ로 발행자 확인 기능 켜기
        message: Message = create_message()
        if message.publish('chapter4-example', 'important.message'):
            print('The message was confirmed')
