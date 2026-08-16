from django.urls import path
from . import views
from rest_framework.authtoken import views as token_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('' , views.BookApiView.as_view()),
    # path('' , views.BookListView.as_view()),
    path('user/' , views.UserInfoApiView.as_view()),
    path('api-token-auth/' , token_views.obtain_auth_token),
    path('b/<int:pk>' , views.BookManageApiView.as_view()),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/logout/' , views.LogoutApiView.as_view() , name='logout'),
 ] 

router = DefaultRouter()
router.register('books' , views.BookListView , basename='books')
urlpatterns += router.urls
