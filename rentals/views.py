from itertools import product
from .models import Dress
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    """
    Display all available dresses on the homepage.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered homepage with available dresses.
    """
    dresses = Dress.objects.filter(available=True)
    return render(request, 'rentals/home.html', {'dresses': dresses})

def about(request):
    """
    Display the static About page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered About page.
    """
    return render(request, 'rentals/about.html')

def register(request):
    """
    Handle user registration using Django's built-in UserCreationForm.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered registration form or redirect on success.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rentals:login')  
    else:
        form = UserCreationForm()
    return render(request, 'rentals/register.html', {'form': form})

def login_view(request):
    """
    Authenticate and log in the user.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered login form or redirect on successful login.
    """
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

def logout_view(request):
    """
    Log out the current user and redirect to the login page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Redirect to login page after logout.
    """
    logout(request)
    return redirect('rentals:login')  
