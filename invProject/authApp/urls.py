from django.urls import path
from . import views

#namespace
app_name = "authApp"

urlpatterns = [
    path("", views.home_view, name="dashboard"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("protected/", views.ProtectedView.as_view(), name="protected"),
]
