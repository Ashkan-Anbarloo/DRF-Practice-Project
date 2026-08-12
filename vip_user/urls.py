from django.urls import path
from . import views

urlpatterns = [
    path('' , views.VipUserAPIView.as_view() , name='vip_user'),
    path('update_user/<int:pk>' , views.UpdateUserAPIView.as_view() , name='update_user'),
]
