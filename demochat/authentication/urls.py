from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path("info/", UserView.as_view(), name='info'),
    path("test-token/", TestTokenView.as_view(), name='test-token')
]
