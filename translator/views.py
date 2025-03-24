from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages  # For error messages
from .forms import CustomUserCreationForm, CustomLoginForm, AuthenticationForm  # Import custom forms
import subprocess  # Import subprocess for running the GUI script
import os

def landing(request):
    return render(request, 'translator/landing.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('translator:login')  # Redirect to login after registering
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'translator/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('translator:home')  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'translator/login.html', {'form': form})

def home(request):
    return render(request, 'translator/home.html')

def logout_view(request):
    logout(request)
    return redirect('translator:landing')  # Redirect to landing page

# ✅ Fix: Open GUI correctly when clicking TRANSLATE button
def translate(request):
    try:
        script_path = os.path.join(os.path.dirname(__file__), "final_pred.py")  # Get absolute path
        script_dir = os.path.dirname(script_path)  # Get script directory

        # Run the script with the correct working directory
        subprocess.Popen(["python", script_path], cwd=script_dir, shell=True)
        
    except Exception as e:
        messages.error(request, f"Error starting translation: {e}")

    return redirect('translator:home')

