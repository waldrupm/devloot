from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('assets/', views.single_asset),
]
