from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Nouvelle URL pour la racine
    path('display_guest_data/', views.display_guest_data, name='display_guest_data'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('login_redirect/', views.login_redirect, name='login_redirect'),
    path('display_booking_value/', views.display_booking_value, name='display_booking_value'),
    path('display_mcom/', views.display_mcom, name='display_mcom'),
]
