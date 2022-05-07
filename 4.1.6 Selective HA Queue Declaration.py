from typing import Dict

import rabbitpy
from rabbitpy import Connection, Channel, Queue

connection: Connection = rabbitpy.Connection()
try:
    channel: Channel
    with connection.channel() as channel:
        arguments: Dict[str, object] = {'x-ha-policy': 'nodes',
                                        'x-ha-nodes': ['rabbit@node1',
                                                       'rabbit@node2',
                                                       'rabbit@node3']}
        queue: Queue = rabbitpy.Queue(channel, 'my-2nd-ha-queue', arguments=arguments)

        if queue.declare():
            print('Queue  declared')
except rabbitpy.exceptions.RemoteClosedChannelException as error:
    print('Queue declare failed: %s' % error)
