from django.shortcuts import render
from .models import Asset
from django.views.generic import ListView, DetailView


# Create your views here.
class AssetList(ListView):
    model = Asset


class AssetDetail(DetailView):
    model = Asset
