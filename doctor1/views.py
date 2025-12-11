'''from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Doctor
from .forms import DoctorForm

class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'
    template_name = 'doctor1/doctor_list.html'

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor1/doctor_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor1/doctor_form.html'
    success_url = reverse_lazy('doctor-list')

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctor1/doctor_form.html'
    success_url = reverse_lazy('doctor-list')

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctor1/doctor_confirm_delete.html'
    success_url = reverse_lazy('doctor-list')


'''

'''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Doctor
from .forms import DoctorForm

# ---------------------------------------------------
# DOCTOR DASHBOARD (doctor only)
# ---------------------------------------------------
@login_required
def doctor_dashboard(request):
    if request.user.role != "doctor":
        return redirect("login")

    # If doctor profile not created yet → force create
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect("doctor-add")

    return render(request, "doctor1/dashboard.html", {"doctor": doctor})


# ---------------------------------------------------
# ADMIN: ADD DOCTOR PROFILE
# ---------------------------------------------------
@login_required
def doctor_add(request):
    if request.user.role != "admin":
        return redirect("login")

    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = None   # Admin creates doctor profile (not linked)
            doctor.save()
            return redirect("doctor-list")
    else:
        form = DoctorForm()

    return render(request, "doctor1/doctor_form.html", {"form": form})


# ---------------------------------------------------
# ADMIN: VIEW ALL DOCTORS
# ---------------------------------------------------
@login_required
def doctor_list(request):
    if request.user.role != "admin":
        return redirect("login")

    doctors = Doctor.objects.all()
    return render(request, "doctor1/doctor_list.html", {"doctors": doctors})


# ---------------------------------------------------
# DOCTOR: EDIT OWN PROFILE
# ---------------------------------------------------
@login_required
def doctor_edit(request):
    if request.user.role != "doctor":
        return redirect("login")

    doctor = get_object_or_404(Doctor, user=request.user)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor-dashboard")
    else:
        form = DoctorForm(instance=doctor)

    return render(request, "doctor1/doctor_form.html", {"form": form})


# ---------------------------------------------------
# ADMIN: DELETE DOCTOR
# ---------------------------------------------------
@login_required
def doctor_delete(request, pk):
    if request.user.role != "admin":
        return redirect("login")

    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect("doctor-list")  '''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .models import Doctor
from .forms import DoctorForm


# ---------------------------------------------------
# DOCTOR DASHBOARD (doctor only)
# ---------------------------------------------------
@login_required
def doctor_dashboard(request):
    if request.user.role != "doctor":
        return redirect("login")

    # Try to get linked doctor profile
    doctor = Doctor.objects.filter(user=request.user).first()

    if not doctor:
        # If doctor profile missing, redirect to edit/create form
        return redirect("doctor-edit")

    return render(request, "doctor1/dashboard.html", {"doctor": doctor})


# ---------------------------------------------------
# DOCTOR: CREATE OR EDIT OWN PROFILE
# ---------------------------------------------------
@login_required
def doctor_edit(request):
    if request.user.role != "doctor":
        return redirect("login")

    # Get or create doctor profile linked to this user
    doctor, created = Doctor.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor-dashboard")
    else:
        form = DoctorForm(instance=doctor)

    return render(request, "doctor1/doctor_form.html", {"form": form})


# ---------------------------------------------------
# ADMIN: ADD DOCTOR PROFILE (not linked to user)
# ---------------------------------------------------
@login_required
def doctor_add(request):
    if request.user.role != "admin":
        return redirect("login")

    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.user = None  # Admin creates doctor profile without user link
            doctor.save()
            return redirect("doctor-list")
    else:
        form = DoctorForm()

    return render(request, "doctor1/doctor_form.html", {"form": form})


# ---------------------------------------------------
# ADMIN: VIEW ALL DOCTORS
# ---------------------------------------------------
'''@login_required
def doctor_list(request):
    if request.user.role != "admin":
        return redirect("login")

    doctors = Doctor.objects.all()
    return render(request, "doctor1/doctor_list.html", {"doctors": doctors})
'''

#@login_required
def doctor_list(request):
    # Allow admin and doctors to see the doctor list
    if request.user.role not in ["admin", "doctor",'patient']:
        return redirect("login")

    doctors = Doctor.objects.all()
    return render(request, "doctor1/doctor_list.html", {"doctors": doctors})



# ---------------------------------------------------
# ADMIN: DELETE DOCTOR
# ---------------------------------------------------
@login_required
def doctor_delete(request, pk):
    if request.user.role != "admin":
        return redirect("login")

    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect("doctor-list")


@login_required
def doctor_edit_by_admin(request, pk):
    if request.user.role != "admin":
        return redirect("login")

    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == "POST":
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctor-list")
    else:
        form = DoctorForm(instance=doctor)

    return render(request, "doctor1/doctor_form.html", {"form": form})


