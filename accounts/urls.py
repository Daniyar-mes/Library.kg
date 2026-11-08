from django.urls import path
from .views import (
    register_view, 
    verify_code_view, 
    auth_login_view, 
    auth_logout_view, 
    profile_view
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('verify/', verify_code_view, name='verify'),
    path('login/', auth_login_view, name='login'),
    path('logout/', auth_logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
