from django.urls import path

from accounts.views import LoginView, RegisterView


urlpatterns = [
    path('',  LoginView.as_view(), name='post_list_url'),
    path('register/', RegisterView.as_view(), name='register_url'),

]