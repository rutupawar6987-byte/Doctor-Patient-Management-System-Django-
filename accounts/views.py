'''from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from doctor1.models import Doctor  # Import Doctor model

def register(request):
    """
    Handle user registration.
    On POST, validate and create user, then log them in and redirect based on role.
    On GET, show the registration form.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Auto-create Doctor profile if user.role == 'doctor'
            if user.role == 'doctor':
                Doctor.objects.get_or_create(
                    user=user,
                    defaults={
                        'first_name': user.username,  # or customize
                        'email': user.email,
                        'specialization': 'general',  # default or blank
                    }
                )

            login(request, user)
            return redirect('role_redirect')  # Name of the URL pattern for role_redirect
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


def role_redirect(request):
    """
    Redirect users to their respective dashboards based on their role.
    """
    user = request.user

    if user.role == 'doctor':
        return redirect('doctor-dashboard')  # Match the URL name in doctor1.urls.py

    elif user.role == 'patient':
        return redirect('patient-dashboard')  # Make sure this URL name exists in patient1.urls.py

    elif user.role == 'admin':
        return redirect('admin-dashboard')  # Adjust if you have a custom admin dashboard URL

    # Default fallback
    return redirect('/') '''

'''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from doctor1.models import Doctor

def register(request):
    """
    Handle user registration.
    On POST, validate and create user, then redirect to login (no auto login).
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Auto-create Doctor profile if user.role == 'doctor'
            if user.role == 'doctor':
                Doctor.objects.get_or_create(
                    user=user,
                    defaults={
                        'first_name': user.username,
                        'email': user.email,
                        'specialization': 'general',
                    }
                )

            # Redirect to login page after registration (no auto-login)
            return redirect('login')

        else:
            # form is invalid, render with errors
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})


@login_required
def role_redirect(request):
    user = request.user
    if user.role == 'doctor':
        return redirect('doctor-dashboard')
    elif user.role == 'patient':
        return redirect('patient-dashboard')
    elif user.role == 'admin':
        return redirect('admin-dashboard')
    else:
        return redirect('/')
'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from doctor1.models import Doctor

def register(request):
    """
    Handle user registration.
    On POST, validate and create user, then redirect to login (no auto login).
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Auto-create Doctor profile if user.role == 'doctor'
            if user.role == 'doctor':
                Doctor.objects.get_or_create(
                    user=user,
                    defaults={
                        'first_name': user.username,
                        'email': user.email,
                        'specialization': 'general',
                    }
                )

            return redirect('login')  # Redirect to login
        else:
            return render(request, 'registration/register.html', {'form': form})

    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


'''@login_required
def role_redirect(request):
    user = request.user
    if user.role == 'doctor':
        return redirect('doctor-dashboard')
    elif user.role == 'patient':
        return redirect('patient-dashboard')
    elif user.role == 'admin':
        return redirect('admin-dashboard')
    return redirect('/')  '''

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from patient1.models import Patient

@login_required
def role_redirect(request):
    user = request.user
    if user.role == 'doctor':
        return redirect('doctor-dashboard')
    elif user.role == 'patient':
        # Check if patient profile exists
        try:
            patient = user.patient  # related_name='patient' from OneToOneField
            return redirect('patient-dashboard')
        except Patient.DoesNotExist:
            # If patient profile doesn't exist, send to patient edit form
            return redirect('patient-edit')
    elif user.role == 'admin':
        return redirect('admin-dashboard')
    return redirect('/')
