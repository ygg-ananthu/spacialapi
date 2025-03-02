# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from spatialdata.models import SpatialPoint, SpatialPolygon
# Register your models here.
admin.site.register(SpatialPoint)
admin.site.register(SpatialPolygon)

