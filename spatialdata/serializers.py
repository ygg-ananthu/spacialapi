from rest_framework_gis import serializers
from .models import SpatialPoint, SpatialPolygon

class SpatialPointSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = SpatialPoint
        geo_field = 'location'
        fields = ('id', 'name', 'description', 'created_at')

class SpatialPolygonSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = SpatialPolygon
        geo_field = 'area'
        fields = ('id', 'name', 'population_density', 'created_at')