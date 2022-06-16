
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('',OverViewList.as_view(),name='home'),
    path('user_registration',Registration.as_view(), name='user_registration'),
    path('user_login', UserLogin.as_view(), name='login'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'), 
    path('tag_create',TagCreate.as_view(),  name="tag_create"),
    path('detail_user_tag_list/<pk>',UserTagDetail.as_view(),  name="detail_user_tag_list"),
    path('update_user_tag/<pk>',UpdateUserTag.as_view(),  name="update_user_tag"),
    path('delete_user_tag/<pk>',DeleteUserTag.as_view(),  name="delete_user_tag"),
    path('tag_list',TagList.as_view(),  name="tag_list"),
    path('detail_tag_list/<pk>',TagDetail.as_view(),  name="detail_tag_list"),


]
