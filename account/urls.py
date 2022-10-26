from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logon', views.logon, name='logon'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('authview', views.authview, name='authview'),
]
