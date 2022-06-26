import json

from rest_framework import status
from core.models import URLShortener
from rest_framework.test import APITestCase
from copy import deepcopy


class TestUrlListAPI(APITestCase):
    """
        Url Shortener POST Api Test Cases
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = '/api/v1/all-url/'

    def prepare_data(self):
        self.data1 = {
            "id": 100001,
            "url": "https://furkanozkaya.com/devops/helm-nedir-nasil-kullanilir/",
            "short_url": "AFO1",
            "visitor": 10
        }
        self.data2 = {
            "id": 100002,
            "url": "https://furkanozkaya.com/software-languages/dependency-injection-vs-dependency-inversion/",
            "short_url": "AF02",
            "visitor": 99
        }
        URLShortener.objects.mongo_insert_many(deepcopy([self.data1, self.data2]))

    def test_200_case1(self):
        self.prepare_data()
        expected_data = [self.data1, self.data2]

        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = json.loads(json.dumps(response.data))
        self.assertEqual(res_data, expected_data)

    def test_204_case1(self):
        expected_data = []
        URLShortener.objects.all().delete()
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        res_data = json.loads(json.dumps(response.data))
        self.assertEqual(res_data, expected_data)

    def test_405_case_post(self):
        response = self.client.post(self.url, format="json")
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
