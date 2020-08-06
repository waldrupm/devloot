from django.shortcuts import render
from .models import Asset


# Create your views here.
def home(request):
    assets = Asset.objects.all()
    context = {'assets': assets}
    return render(request, 'assets/home.html', context=context)


def single_asset(request):
    return render(request, 'assets/single.html')
