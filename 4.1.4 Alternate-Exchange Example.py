from typing import Dict

import rabbitpy
from rabbitpy import Channel, Exchange, Queue

with rabbitpy.Connection() as connection:
    channel: Channel
    with connection.channel() as channel:
        # fanout 익스체인지는 자신이 알고 있는 모든 큐에 메시지를 전달
        # topic 익스체인지는 라우팅 키를 기반으로 선택적으로 메시지를 라우팅
        my_ae: Exchange = rabbitpy.Exchange(channel, 'my-ae', exchange_type='fanout')  # 대체 익스체인지를 선언하기 위한 객체 생성
        my_ae.declare()  # 대체 익스체인지 선언

        args: Dict[str, object] = {'alternate-exchange': my_ae.name}

        exchange: Exchange = rabbitpy.Exchange(channel, 'graphite', exchange_type='topic', arguments=args)
        exchange.declare()
        queue: Queue = rabbitpy.Queue(channel, 'unroutable-messages')  # 큐 객체 생성
        queue.declare()  # 큐 선언
        if queue.bind(my_ae, '#'):
            print('Queue bound to alternate-exchange')
