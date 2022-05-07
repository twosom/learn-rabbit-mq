import rabbitpy
from rabbitpy import Channel, Message

with rabbitpy.Connection() as connection:
    channel: Channel
    with connection.channel() as channel:
        tx = rabbitpy.Tx(channel)
        tx.select()

        message: Message = rabbitpy.Message(channel, 'This is an important message',
                                            {'content_type': 'text/plain', 'delivery_mode': 2,
                                             'message_type': 'important'})
        message.publish('chapter4-example', 'important.message')
        try:
            if tx.commit():
                print('Transaction committed')
        except rabbitpy.exceptions.NoActiveTransactionError:
            print('Tried to commit without active transaction')

