from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('' , views.BookApiView.as_view()),
    path('user/' , views.UserInfoApiView.as_view()),
    path('api-token-auth/' , token_views.obtain_auth_token),
    path('b/<int:pk>' , views.BookManageApiView.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
