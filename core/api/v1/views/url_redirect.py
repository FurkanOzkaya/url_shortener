from rest_framework.views import APIView
from common.decarators import validatorV1
from core.api.v1.common.common_functions import short_url_to_id
from core.api.v1.common.request_serializer import UrlRedirectSerializer


from core.models import URLShortener
from django.http import HttpResponseRedirect


class UrlRedirectAPI(APIView):
    """
    Redirect Short Url to Long Url
    """
    @validatorV1(path_validator=UrlRedirectSerializer)
    def get(self, _, path_serializer, *args, **kwargs):
        id = short_url_to_id(path_serializer.validated_data.get("url"))
        # update when fetching long url
        res = URLShortener.objects.mongo_find_one_and_update({"id": id}, {"$inc": {"visitor": 1}}, {"_id": 0})

        return HttpResponseRedirect(res.get("url"))
