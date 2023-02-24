from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/register/", views.login_register_user, name="login_register_user"),
    path("logout/", views.logout_user, name="logout_user"),
]