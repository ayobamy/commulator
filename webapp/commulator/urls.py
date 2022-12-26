from django.urls import path
from .views import signup, base, login

app_name = "commulator"

urlpatterns = [
    path("", base, name="base"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
]