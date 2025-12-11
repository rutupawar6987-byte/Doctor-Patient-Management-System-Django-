'''from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Patient, PatientHistory
from .forms import PatientForm, PatientHistoryForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

# ----------------------
# Patient Views
# ----------------------

class PatientListView(ListView):
    model = Patient
    template_name = 'patient1/patient_list.html'  # your template path
    context_object_name = 'patients'  # context variable in template


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient1/patient_detail.html'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient1/patient_form.html'
    success_url = reverse_lazy('patient-list')


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient1/patient_form.html'
    success_url = reverse_lazy('patient-list')


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient1/patient_confirm_delete.html'
    success_url = reverse_lazy('patient-list')


# ----------------------
# PatientHistory Views
# ----------------------

# ----------------------
# PatientHistory Views
# ----------------------

class PatientHistoryListView(ListView):
    model = PatientHistory
    template_name = 'patient1/patienthistory_list.html'
    context_object_name = 'histories'

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientHistory.objects.filter(patient_id=patient_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient_id = self.kwargs['patient_id']
        context['patient'] = get_object_or_404(Patient, pk=patient_id)
        return context


class PatientHistoryDetailView(DetailView):
    model = PatientHistory
    template_name = 'patient1/patienthistory_detail.html'

class PatientHistoryCreateView(CreateView):
    model = PatientHistory
    form_class = PatientHistoryForm
    template_name = 'patient1/patienthistory_form.html'

    def form_valid(self, form):
        # attach patient ID from URL parameter patient_id
        form.instance.patient = get_object_or_404(Patient, pk=self.kwargs['patient_id'])
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to history list of the patient
        return reverse_lazy('patienthistory-list', kwargs={'patient_id': self.kwargs['patient_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass patient_id so your template can reverse URLs correctly
        context['patient_id'] = self.kwargs['patient_id']
        context['patient'] = get_object_or_404(Patient, pk=self.kwargs['patient_id'])
        return context


class PatientHistoryUpdateView(UpdateView):
    model = PatientHistory
    form_class = PatientHistoryForm
    template_name = 'patient1/patienthistory_form.html'

    def get_success_url(self):
        return reverse_lazy('patienthistory-list', kwargs={'patient_id': self.object.patient.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = self.object.patient
        return context


class PatientHistoryDeleteView(DeleteView):
    model = PatientHistory
    template_name = 'patient1/patienthistory_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('patienthistory-list', kwargs={'patient_id': self.object.patient.pk})
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Patient, PatientHistory
from .forms import PatientForm, PatientHistoryForm
from doctor1.models import Doctor

# Decorator for class-based views
def patient_required(view_func):
    decorated_view_func = login_required(view_func)

    def _wrapped_view(request, *args, **kwargs):
        if request.user.role != 'patient':
            return redirect('login')
        return decorated_view_func(request, *args, **kwargs)

    return _wrapped_view

# ----- Patient CRUD Views -----

@method_decorator(login_required, name='dispatch')
class PatientListView(ListView):
    model = Patient
    template_name = 'patient1/patient_list.html'
    context_object_name = 'patients'

@method_decorator(login_required, name='dispatch')
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient1/patient_detail.html'

@method_decorator(login_required, name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient1/patient_form.html'
    success_url = reverse_lazy('patient-list')

@method_decorator(login_required, name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient1/patient_form.html'
    success_url = reverse_lazy('patient-list')

@method_decorator(login_required, name='dispatch')
class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'patient1/patient_confirm_delete.html'
    success_url = reverse_lazy('patient-list')


# ----- Patient History Views -----

@method_decorator(login_required, name='dispatch')
class PatientHistoryListView(ListView):
    model = PatientHistory
    template_name = 'patient1/patienthistory_list.html'
    context_object_name = 'histories'

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientHistory.objects.filter(patient_id=patient_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = get_object_or_404(Patient, pk=self.kwargs['patient_id'])
        return context

@method_decorator(login_required, name='dispatch')
class PatientHistoryDetailView(DetailView):
    model = PatientHistory
    template_name = 'patient1/patienthistory_detail.html'

@method_decorator(login_required, name='dispatch')
class PatientHistoryCreateView(CreateView):
    model = PatientHistory
    form_class = PatientHistoryForm
    template_name = 'patient1/patienthistory_form.html'

    def form_valid(self, form):
        form.instance.patient = get_object_or_404(Patient, pk=self.kwargs['patient_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('patienthistory-list', kwargs={'patient_id': self.kwargs['patient_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_id'] = self.kwargs['patient_id']
        context['patient'] = get_object_or_404(Patient, pk=self.kwargs['patient_id'])
        return context

@method_decorator(login_required, name='dispatch')
class PatientHistoryUpdateView(UpdateView):
    model = PatientHistory
    form_class = PatientHistoryForm
    template_name = 'patient1/patienthistory_form.html'

    def get_success_url(self):
        return reverse_lazy('patienthistory-list', kwargs={'patient_id': self.object.patient.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = self.object.patient
        return context

@method_decorator(login_required, name='dispatch')
class PatientHistoryDeleteView(DeleteView):
    model = PatientHistory
    template_name = 'patient1/patienthistory_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('patienthistory-list', kwargs={'patient_id': self.object.patient.pk})


# ----- Patient Dashboard & Edit Profile Views -----

@login_required
def patient_dashboard(request):
    if request.user.role != 'patient':
        return redirect('login')

    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        return redirect('patient-edit')

    doctors = Doctor.objects.all()
    return render(request, 'patient1/dashboard.html', {
        'patient': patient,
        'doctors': doctors,
    })


@login_required
def patient_edit(request):
    if request.user.role != 'patient':
        return redirect('login')

    try:
        patient = request.user.patient
    except Patient.DoesNotExist:
        patient = None

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            p = form.save(commit=False)
            p.user = request.user
            p.save()
            return redirect('patient-dashboard')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patient1/patient_form.html', {'form': form})

'''@login_required
def patient_edit(request, pk):
    if request.user.role != 'patient':
        return redirect('login')

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient-detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)

    return render(request, 'patient1/patient_form.html', {'form': form})

'''