from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views


urlpatterns = [
    path('' , views.BookApiView.as_view()),
    path('user/' , views.UserInfoApiView.as_view()),
    path('api-token-auth/' , token_views.obtain_auth_token),
    path('b/<int:pk>' , views.BookManageApiView.as_view()),
]
