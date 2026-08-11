from django.urls import path
from . import views

urlpatterns = [
    path('' , views.VipUserAPIView.as_view() , name='vip_user'),
]
