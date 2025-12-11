'''from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor-list'),  # this handles /doctor1/
    path('add/', DoctorCreateView.as_view(), name='doctor-add'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('<int:pk>/edit/', DoctorUpdateView.as_view(), name='doctor-edit'),
    path('<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor-delete'),
]
'''
from django.urls import path
from .views import (
    doctor_dashboard,
    doctor_add,
    doctor_list,
    doctor_edit,
    doctor_edit_by_admin,   # <-- add this
    doctor_delete
)

urlpatterns = [

    # Doctor Dashboard (doctor only)
    path('dashboard/', doctor_dashboard, name='doctor-dashboard'),

    # Admin: add doctor
    path('add/', doctor_add, name='doctor-add'),

    # Admin: list all doctors
    path('list/', doctor_list, name='doctor-list'),

    # Doctor: edit own profile
    path('edit/', doctor_edit, name='doctor-edit'),

    # Admin: edit any doctor profile by pk
    path('<int:pk>/edit/', doctor_edit_by_admin, name='doctor-edit-by-admin'),

    # Admin: delete doctor
    path('<int:pk>/delete/', doctor_delete, name='doctor-delete'),
]
