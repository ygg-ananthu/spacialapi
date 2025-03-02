from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from spatialdata import views

router = routers.DefaultRouter()
router.register(r'points', views.SpatialPointViewSet)
router.register(r'polygons', views.SpatialPolygonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]