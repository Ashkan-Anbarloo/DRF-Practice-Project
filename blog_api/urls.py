from django.urls import path
from . import views

urlpatterns = [
    path('fbv' , views.hello_world),
    path('cbv' , views.HelloAPIView.as_view()),
]
