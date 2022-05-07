import rabbitpy
from rabbitpy import Connection, Channel, Queue

connection: Connection = rabbitpy.Connection()
try:
    channel: Channel
    with connection.channel() as channel:
        queue: Queue = rabbitpy.Queue(channel, 'my-ha-queue',
                                      arguments={'x-ha-policy': 'all'})  # Queue 객체의 새 인스턴스를 만들고 HA 정책을 전달한다.
        if queue.declare():
            print('Queue declared')
except rabbitpy.exceptions.RemoteClosedChannelException as error:
    print('Queue declare failed: %s' % error)
