from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'assets/home.html')


def single_asset(request):
    return render(request, 'assets/single.html')
