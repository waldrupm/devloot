from django.urls import path
from . import views


app_name = "assets"
urlpatterns = [
    path("", views.AssetList.as_view(), name="AssetList"),
    path("asset/<int:pk>", views.AssetDetail.as_view(), name="AssetDetail"),
]
