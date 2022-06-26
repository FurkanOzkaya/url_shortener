import json

from unittest.mock import patch
from rest_framework import status
from core.models import URLShortener
from rest_framework.test import APITestCase


class CounterMock():
    def __init__(self) -> None:
        self.value = 10001
        self.pre_value = 10000

    def __add__(self, a):
        self.pre_value += self.value
        self.value += a
        return self

    def __sub__(self, a):
        self.pre_value += self.value
        self.value -= a
        return self


class InstanceMock():
    def Counter(self, path) -> None:
        return CounterMock()


class ZooKeeperMock():
    def __init__(self):
        self.instance = InstanceMock()


class TestUrlShortenerAPI(APITestCase):
    """
        Url Shortener POST Api Test Cases
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = '/api/v1/url-shortener/'

    @patch("core.api.v1.views.url_shortener.ZooKeeper")
    def test_200_case1(self, mock):
        mock.return_value = ZooKeeperMock()
        expected_data = {'short_url': "http://localhost:8000/0005Cb"}

        response = self.client.post(self.url, data={"url": "http://furkanozkaya.com"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = json.loads(json.dumps(response.data))
        self.assertEqual(res_data, expected_data)

    def test_405_case_get(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_405_case_patch(self):
        response = self.client.patch(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_405_case_delete(self):
        response = self.client.delete(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    @classmethod
    def tearDownClass(cls) -> None:
        URLShortener.objects.all().delete()
        return super().tearDownClass()
