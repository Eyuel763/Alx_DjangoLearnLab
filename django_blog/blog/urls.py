from django.urls import path
from . import views
from django.contrib.auth import views as auth_views #import built-in auth views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]