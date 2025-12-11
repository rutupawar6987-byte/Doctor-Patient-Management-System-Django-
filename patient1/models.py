from django.db import models
from django.conf import settings  # for referencing AUTH_USER_MODEL


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient',
        null=False,    # temporarily nullable for migrations
        blank=False,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth")
    gender_choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    gender = models.CharField(max_length=1, choices=gender_choices)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PatientHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='histories')
    visit_date = models.DateField()

    # New fields for patient-reported vitals
    blood_pressure = models.CharField(max_length=20, blank=True, null=True, help_text="Patient's blood pressure")
    blood_sugar = models.CharField(max_length=20, blank=True, null=True, help_text="Patient's blood sugar level")
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Weight in kg")
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, help_text="Height in cm")
    temperature = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, help_text="Body temperature in °C")
    
    blood_group_choices = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, choices=blood_group_choices, blank=True, null=True, help_text="Blood group")

    def __str__(self):
        return f"Vitals of {self.patient} on {self.visit_date}"
