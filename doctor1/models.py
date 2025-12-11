'''from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('dermatology', 'Dermatology'),
        ('general', 'General Medicine'),
        ('ot', 'OT'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES,
        default='general'
    )
    qualification = models.CharField(max_length=200, blank=True, null=True)
    hospital = models.CharField(max_length=200, blank=True, null=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    working_time = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.get_specialization_display()})"

'''

from django.db import models
from accounts.models import User   # ADD THIS

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # ^ This links doctor to the logged-in user

    SPECIALIZATION_CHOICES = [
        ('cardiology', 'Cardiology'),
        ('neurology', 'Neurology'),
        ('pediatrics', 'Pediatrics'),
        ('orthopedics', 'Orthopedics'),
        ('dermatology', 'Dermatology'),
        ('general', 'General Medicine'),
        ('ot', 'OT'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(
        max_length=50,
        choices=SPECIALIZATION_CHOICES,
        default='general'
    )
    qualification = models.CharField(max_length=200, blank=True, null=True)
    hospital = models.CharField(max_length=200, blank=True, null=True)
    ratings = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    working_time = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} ({self.get_specialization_display()})"

