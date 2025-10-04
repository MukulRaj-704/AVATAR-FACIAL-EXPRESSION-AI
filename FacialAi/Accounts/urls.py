from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_user', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create-profile/', views.create_profile_view, name='create_profile'),
]
