from django.urls import path

from . import views

urlpatterns = [path(r"api/", views.api, name="api")]
