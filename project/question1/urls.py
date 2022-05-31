from django.urls import path, include, re_path as url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'vehicle', views.VehicleViewSet)
router.register(r'navigation_record', views.NavigationRecordViewSet)



app_name = 'question1'

urlpatterns = [
    path("", include(router.urls))
]
