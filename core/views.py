from django.contrib.auth.models import User 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment
import os
from django.conf import settings
from .forms import AppointmentForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointment_list.html', {'appointments': appointments})

@login_required(login_url='login')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('appointment_list')  # Redirect to the appointment list page or another appropriate page
        else:
            messages.error(request, 'Failed to book appointment. Please correct the errors.')
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
        
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                # Send a welcome message to the user
                messages.success(request, f"Welcome, {username}!")
                return redirect('/')
            except:
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('/')