from django.db import models


# Create your models here.

class CurrentList(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class FavoriteList(models.Model):
    farm = models.BigIntegerField()
    id = models.BigIntegerField(primary_key=True)
    server = models.BigIntegerField()
    secret = models.CharField(max_length=256)
    title = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return str(self.id)
