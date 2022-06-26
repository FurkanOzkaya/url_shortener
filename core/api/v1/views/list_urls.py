from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from core.models import URLShortener


class ListInformationsAPI(APIView):
    """
    List All Informations
    """

    def get(self, _, *args, **kwargs):
        res = list(URLShortener.objects.mongo_find({}, {"_id": 0}))
        if res:
            return Response(data=res, status=status.HTTP_200_OK)
        return Response(data=res, status=status.HTTP_204_NO_CONTENT)
