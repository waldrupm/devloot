from django.shortcuts import render, redirect
from .models import Asset, FeaturedSet
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .forms import CreateUserForm


# Create your views here.
class AssetList(ListView):
    paginate_by = 10
    model = Asset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['featured_set'] = FeaturedSet.objects.filter(status='active').first()
        return context


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
        messages.success(request, 'User Created')
        return redirect('assets:home')
    else:
        form = CreateUserForm()
    return render(request, 'assets/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('assets:home')
        else:
            messages.info(request, 'Username / password combo incorrect')
    
    return render(request, 'assets/login.html')


def logoutPage(request):
    logout(request)
    return redirect('assets:home')