from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.decarators import validatorV1
from common.zookeeper_handler import ZooKeeper
from core.api.v1.common.common_functions import id_to_short_url, short_url_to_id
from core.api.v1.common.request_serializer import UrlShortenerSerializer


from core.models import URLShortener
from url_shortener.settings import DEFAULT_ID_COUNT, BASE_URL, HOSTNAME, HOST_NUMBER


class UrlShortenerAPI(APIView):
    """
    Create Short Url from Long Url
    """
    @validatorV1(request_type="body", validator=UrlShortenerSerializer)
    def post(self, _, serializer, *args, **kwargs):
        # take counter from zookeper increase one and create short url for long url, write to db and return short url
        zk = ZooKeeper()
        # TODO CHANGE HERE ACCRODING TO ZOOKEEPER
        counter = zk.instance.Counter(f'/{HOSTNAME}')
        counter += 1
        if counter.value >= int(DEFAULT_ID_COUNT) * (int(HOST_NUMBER) + 2):  # final id must be same with other pods start id
            # out of id, change zookeeper id range for this pod, Notify admin this will not implement
            pass
        res = id_to_short_url(counter.pre_value, minlength=6)
        short_url = f"{BASE_URL}/{res}"
        data = {
            "id": counter.pre_value,
            "url": serializer.validated_data.get("url"),
            "short_url": res,
            "visitor": 0  # default 0
        }
        try:
            URLShortener.objects.mongo_insert_one(data)
            return Response({"short_url": short_url}, status=status.HTTP_200_OK)
        except Exception as err:
            return Response(data=err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
