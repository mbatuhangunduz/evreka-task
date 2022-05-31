from django.urls import path, include, re_path as url

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('bin', views.BinViewSet)
router.register('operation', views.OperationViewSet)
router.register('bin-operation', views.BinOperationViewSet)


app_name = 'question2'

urlpatterns = [
    path("", include(router.urls))
]
