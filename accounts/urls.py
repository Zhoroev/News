from django.urls import path

from accounts.views import LoginView, RegisterView, logout_view


urlpatterns = [
    path('',  LoginView.as_view(), name='login_url'),
    path('register/', RegisterView.as_view(), name='register_url'),
    path('logout/', logout_view, name='logout_url')
]