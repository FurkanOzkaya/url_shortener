from django.urls import path
from core.api.v1.views.list_urls import ListInformationsAPI
from core.api.v1.views.url_shortener import UrlShortenerAPI


urlpatterns = [
    path('url-shortener/', UrlShortenerAPI.as_view()),
    path('all-url/', ListInformationsAPI.as_view()),
]
