from django.core.management.base import BaseCommand

from common.zookeeper_handler import ZooKeeper
from url_shortener.settings import HOST_NUMBER, DEFAULT_ID_COUNT, HOSTNAME


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            zk = ZooKeeper()
            counter = zk.instance.Counter(f"/{HOSTNAME}")
            if counter.value <= 0:
                # HOST_NUMBER is app-1 1,2,3,4 increasing number
                counter += int(DEFAULT_ID_COUNT) * (int(HOST_NUMBER) + 1)
                print(f"SUCCESS counter {HOST_NUMBER} created => {counter.value}")
            else:
                print(f"SUCCESS Already counter{HOST_NUMBER} exists => {counter.value}")
        except Exception as err:
            print(err)
