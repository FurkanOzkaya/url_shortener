from django.db import models
from djongo.models import DjongoManager
# Create your models here.


class URLShortener(models.Model):
    objects = DjongoManager()

    class Meta:
        db_table = 'url'
