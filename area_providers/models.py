# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.gis.db import models

User._meta.get_field('email')._unique = True


# Create your models here.


class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    language = models.CharField(max_length=20)
    currency = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    polygon = models.MultiPolygonField()  # The Provider can have multiple service areas across the world
    objects = models.GeoManager()

    def __unicode__(self):
        return 'service area for {0}'.format(self.provider.name)
