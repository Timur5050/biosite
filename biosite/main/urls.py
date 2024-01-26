from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="main"),
    path("", views.index, name="about"),
    path("", views.index, name="background"),
    path("", views.index, name="contact"),
]