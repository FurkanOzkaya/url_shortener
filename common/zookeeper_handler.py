from kazoo.client import KazooClient, KazooState
from common.singleton import Singleton
from django.conf import settings


class ZooKeeper(metaclass=Singleton):
    def __init__(self):
        self.instance = KazooClient(hosts=f"{settings.ZOOKEEPER_HOST}:{settings.ZOOKEEPER_PORT}")
        print(f"{settings.ZOOKEEPER_HOST}:{settings.ZOOKEEPER_PORT}")
        self.instance.start()
        # self.instance.add_listener(self.listener)

    def listener(self, state):
        if state == KazooState.LOST:
            # Register somewhere that the session was lost
            exit(1)  # pod will restart
        elif state == KazooState.SUSPENDED:
            # Handle being disconnected from Zookeeper
            exit(1)  # pod will restart
        else:
            # Handle being connected/reconnected to Zookeeper
            exit(1)  # pod will restart
