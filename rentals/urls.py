# rentals/urls.py
from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
    path('', views.home, name='home'),  # Home page at the root URL
    path('about/', views.about, name='about'),  # About page URL
    path('contact/', views.contact, name='contact'),  # Contact page URL
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),   # Login page URL
    path('register/', views.register, name='register'),  # Registration page URL
]
