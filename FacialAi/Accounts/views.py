from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .forms import CustomRegisterForm
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created! Please complete your profile.")
            return redirect('create_profile')
        else:
            # If passwords don't match or any error
            if "Passwords do not match" in str(form.errors):
                messages.error(request, "Passwords do not match")
            else:
                for error in form.errors.values():
                    messages.error(request, error)
            
            # Return a fresh empty form (to clear all fields)
            form = CustomRegisterForm()
    else:
        form = CustomRegisterForm()

    return render(request, 'Accounts/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'Accounts/login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('login')


@login_required

def create_profile_view(request):
    # Get or create profile for logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.email = request.user.email  # auto-fill email
            profile.save()
            messages.success(request, "Profile saved successfully!")
            return redirect('/')  # Redirect to home/dashboard
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'Accounts/create_profile.html', {'form': form})
