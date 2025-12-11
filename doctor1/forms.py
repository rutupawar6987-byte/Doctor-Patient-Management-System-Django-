'''from django import forms
from .models import Doctor
import re

class DoctorForm(forms.ModelForm):
    working_time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': "e.g., 9 AM to 5 PM or 9:30 AM - 5:15 PM",
            'class': 'form-control'
        })
    )

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'qualification', 'specialization', 'hospital', 'ratings', 'email', 'phone', 'working_time']

    def clean_working_time(self):
        working_time = self.cleaned_data.get('working_time')
        pattern = r'^\d{1,2}(:\d{2})?\s?(AM|PM)?\s?(to|-)\s?\d{1,2}(:\d{2})?\s?(AM|PM)?$'
        if working_time:
            if not re.match(pattern, working_time.strip(), re.IGNORECASE):
                raise forms.ValidationError(
                    "Enter working hours in a valid format, e.g., '9 AM to 5 PM' or '9:30 AM - 5:15 PM'."
                )
        return working_time '''

from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        # Add 'form-control' class to each form field widget
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
