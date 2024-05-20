from django.urls import path
from . import views

urlpatterns = [
    path('ReadJson/', views.ReadJson),
    path("visualization/", views.visualization, name = 'visualization'),
]