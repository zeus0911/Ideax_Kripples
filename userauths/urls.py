from django.urls import path
from .views import *

app_name = 'userauths'

urlpatterns = [
    path("sign-up/", register_view, name = "register_view" ),
    path("sign-in/", login_view, name = "login"),
    path("sign-out/", logout_view, name="logout"),
]
