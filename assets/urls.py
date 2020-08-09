from django.urls import path
from . import views


app_name = "assets"
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    
    path("", views.AssetList.as_view(), name="home"),
    path("featured/", views.featured_set, name='featured'),
    path("asset/<int:pk>", views.AssetDetail.as_view(), name="AssetDetail"),
]
