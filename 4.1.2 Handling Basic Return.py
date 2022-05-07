from datetime import datetime
from typing import Dict

import rabbitpy
from rabbitpy import Connection, Message

connection: Connection = rabbitpy.Connection()
try:
    with connection.channel() as channel:
        properties: Dict[str, object] = {'content_type': 'text/plain',
                                         'timestamp': datetime.now(),
                                         'message_type': 'graphite metric'}
        body = 'server .cpu.utilization 25.5 1350884514'
        message: Message = rabbitpy.Message(channel, body, properties)
        message.publish('chapter2-example', 'server-metrics', mandatory=True)
except rabbitpy.exceptions.MessageReturnedException as error:
    print('Publish failure: %s' % error)