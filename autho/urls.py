from django.urls import path
from autho.views import UserLogin, UserRegister, GetRegisteredUser

urlpatterns = [
    path('register/', UserRegister, name='register'),
    path('login/', UserLogin, name='login'),
    path('register-get/', GetRegisteredUser, name='register-get'),
]