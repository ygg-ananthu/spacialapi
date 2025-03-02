from django.contrib.gis.db import models

class SpatialPoint(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SpatialPolygon(models.Model):
    name = models.CharField(max_length=255)
    population_density = models.FloatField()
    area = models.PolygonField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name