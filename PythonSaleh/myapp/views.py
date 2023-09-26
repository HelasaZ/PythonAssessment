from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from .models import Mcom
import requests
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import Group

def home(request):
    return render(request, "home.html")

@login_required
def display_guest_data(request):
    user_type = "user"  # Par défaut, considérez que c'est un utilisateur normal

    if request.user.is_superuser:
        user_type = "superuser"

    if user_type == "superuser":
        guests = Mcom.objects.all()
    else:
        guests = Mcom.objects.values('guest_name', 'status', 'flat_booked', 'checkin_date', 'checkout_date', 'creation_log')

    return render(request, 'guest_data.html', {'guests': guests, 'user_type': user_type})

# Modifier votre vue pour gérer la connexion
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('display_mcom')  # Rediriger vers la vue qui affiche la base de données Mcom
        else:
            # Gérer le cas où l'authentification échoue
            pass
    return render(request, 'login.html')

@login_required()
def display_mcom(request):
    user = request.user
    is_superuser = user.is_superuser

    if is_superuser:
        guests = Mcom.objects.all()
    else:
        guests = Mcom.objects.values('guest_name', 'status', 'flat_booked', 'checkin_date', 'checkout_date', 'creation_log')

    return render(request, 'mcom_display.html', {'guests': guests, 'is_superuser': is_superuser})

@login_required
def profile(request):
    # Ajoutez la logique pour afficher le profil de l'utilisateur
    return render(request, 'profile.html')

@login_required
def login_redirect(request):
    if request.user.is_superuser:
        return redirect('display_guest_data')  # Rediriger vers la vue pour le superutilisateur
    else:
        return redirect('display_booking_value')  # Rediriger vers la vue pour l'utilisateur normal


def display_booking_value(request):
    # Récupérez les données des invités sans booking_value
    guests_without_booking_value = Mcom.objects.values('guest_name', 'status', 'flat_booked', 'checkin_date', 'checkout_date', 'creation_log')

    return render(request, 'booking_value_data.html', {'guests': guests_without_booking_value})





