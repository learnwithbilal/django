from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("humam", views.humam, name="humam"),
    path("ali", views.ali, name="ali"),
    path("<str:name>", views.greet, name="greet")
]
