
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from homes import views

router = routers.DefaultRouter()
router.register(r'houses', views.HouseViewSet)
router.register(r'thermostats', views.ThermostatViewSet)
router.register(r'lights', views.LightViewSet)
router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('authtools.urls')),

    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
