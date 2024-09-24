from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name = "register"),
    path("log_out/", views.log_out, name = "log_out")
    
]
