from django.urls import path

from . import views

urlpatterns = [
    
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('profile', views.home, name="profile"),
    path('user_list', views.user_list, name="user-list"),
    path('user_details/<int:pk>', views.user_details, name="user-details"),
]
