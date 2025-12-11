'''from django.urls import path
from django.views.generic import RedirectView
from .views import (
    PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView,
    PatientHistoryListView, PatientHistoryDetailView, PatientHistoryCreateView,
    PatientHistoryUpdateView, PatientHistoryDeleteView
)

urlpatterns = [

    # Redirect /patient1/ → /patient1/patients/
    path('', RedirectView.as_view(pattern_name='patient-list', permanent=False)),

    # ---------------------------
    # Patient URLs
    # ---------------------------
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/add/', PatientCreateView.as_view(), name='patient-add'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/<int:pk>/edit/', PatientUpdateView.as_view(), name='patient-edit'),
    path('patients/<int:pk>/delete/', PatientDeleteView.as_view(), name='patient-delete'),

    # ---------------------------
    # Patient-Specific History URLs
    # ---------------------------
    path('patients/<int:patient_id>/history/', PatientHistoryListView.as_view(),
         name='patienthistory-list'),

    path('patients/<int:patient_id>/history/add/', PatientHistoryCreateView.as_view(),
         name='patienthistory-add'),

    # ---------------------------
    # Single History Record URLs
    # ---------------------------
    path('history/<int:pk>/', PatientHistoryDetailView.as_view(), name='patienthistory-detail'),
    path('history/<int:pk>/edit/', PatientHistoryUpdateView.as_view(), name='patienthistory-edit'),
    path('history/<int:pk>/delete/', PatientHistoryDeleteView.as_view(), name='patienthistory-delete'),
]  


'''
from django.urls import path
from . import views

urlpatterns = [
    # Patient URLs
    path('', views.PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('add/', views.PatientCreateView.as_view(), name='patient-add'),
    path('edit/<int:pk>/', views.PatientUpdateView.as_view(), name='patient-edit'),
    path('delete/<int:pk>/', views.PatientDeleteView.as_view(), name='patient-delete'),

    # PatientHistory URLs
    path('history/<int:patient_id>/', views.PatientHistoryListView.as_view(), name='patienthistory-list'),
    path('history/detail/<int:pk>/', views.PatientHistoryDetailView.as_view(), name='patienthistory-detail'),
    path('history/add/<int:patient_id>/', views.PatientHistoryCreateView.as_view(), name='patienthistory-add'),
    path('history/edit/<int:pk>/', views.PatientHistoryUpdateView.as_view(), name='patienthistory-edit'),
    path('history/delete/<int:pk>/', views.PatientHistoryDeleteView.as_view(), name='patienthistory-delete'),

    # Patient Dashboard and Profile Edit
    path('dashboard/', views.patient_dashboard, name='patient-dashboard'),
    path('edit/', views.patient_edit, name='patient-edit'),
    #path("edit/<int:pk>/", views.patient_edit, name="patient-edit"),

]
