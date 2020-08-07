from django.shortcuts import render, redirect
from .models import Asset
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate, logout

from .forms import CreateUserForm


# Create your views here.
class AssetList(ListView):
    paginate_by = 10
    model = Asset


class AssetDetail(DetailView):
    model = Asset


def registerPage(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('assets:home')
    else:
        form = CreateUserForm()
    return render(request, 'assets/register.html', {'form': form})


def loginPage(request):
    context = {}
    return render(request, 'assets/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('assets:home')