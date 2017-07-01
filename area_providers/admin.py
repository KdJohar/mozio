# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis import admin

from .models import ServiceArea, Provider

# Register your models here.

admin.site.register(ServiceArea, admin.GeoModelAdmin)
admin.site.register(Provider)
