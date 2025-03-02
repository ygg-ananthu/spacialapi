from rest_framework import viewsets
from .models import SpatialPoint, SpatialPolygon
from .serializers import SpatialPointSerializer, SpatialPolygonSerializer

class SpatialPointViewSet(viewsets.ModelViewSet):
    queryset = SpatialPoint.objects.all()
    serializer_class = SpatialPointSerializer

class SpatialPolygonViewSet(viewsets.ModelViewSet):
    queryset = SpatialPolygon.objects.all()
    serializer_class = SpatialPolygonSerializer