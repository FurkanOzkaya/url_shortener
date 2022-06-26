import json
from rest_framework import status
from core.models import URLShortener
from rest_framework.test import APITestCase
from copy import deepcopy


class TestUrlRedirectAPI(APITestCase):
    """
        Url Shortener POST Api Test Cases
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url = '/'

    def prepare_data(self):
        self.data1 = {
            "id": 10100000,
            "url": "https://furkanozkaya.com/devops/helm-nedir-nasil-kullanilir/",
            "short_url": "00gNTE",
            "visitor": 10
        }
        self.data2 = {
            "id": 10100001,
            "url": "https://furkanozkaya.com/software-languages/dependency-injection-vs-dependency-inversion/",
            "short_url": "00gNTF",
            "visitor": 99
        }
        URLShortener.objects.mongo_insert_many(deepcopy([self.data1, self.data2]))

    def test_200_case1(self):
        self.prepare_data()
        response = self.client.get(f"{self.url}{self.data1['short_url']}", format="json")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        res = list(URLShortener.objects.mongo_find({"short_url": self.data1['short_url']}, {"_id": 0}))
        res = json.loads(json.dumps(res))[0]
        self.assertEqual(res.get("visitor"), self.data1["visitor"] + 1)

    def test_404_case_post(self):
        response = self.client.post(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_404_case_patch(self):
        response = self.client.patch(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_404_case_delete(self):
        response = self.client.delete(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @classmethod
    def tearDownClass(cls) -> None:
        URLShortener.objects.all().delete()
        return super().tearDownClass()
