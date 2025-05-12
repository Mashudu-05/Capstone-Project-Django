from itertools import product
from .models import Dress
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Homepage view — shows all available dresses
def home(request):
    dresses = Dress.objects.filter(available=True)
    return render(request, 'rentals/home.html', {'dresses': dresses})

def about(request):
    return render(request, 'rentals/about.html')

def contact(request):
    return render(request, 'rentals/contact.html')

# User Registration View
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rentals:login')  
    else:
        form = UserCreationForm()
    return render(request, 'rentals/register.html', {'form': form})

# User Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('rentals:home')  
    else:
        form = AuthenticationForm()
    return render(request, 'rentals/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)
    return redirect('rentals:login')  
