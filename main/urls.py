from django.urls import path
from . import views
from authentication.views import log_out

urlpatterns = [
    path("", views.index, name="index"),
    path("send_message/", views.send_message, name="send"),
    path("history/", views.history, name = "history"),
    path("send_to_telegram/", views.send_to_telegram, name = "telegram"),
    path("log_out/", log_out, name = "log_out")
]
