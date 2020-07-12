from django.urls import path
from . import views

urlpatterns = [
    path('base', views.index),
    path('', views.deals_upload, name="deals_upload"),
    path('111', views.top, name="top"),
]