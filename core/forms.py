from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment
from datetime import date

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_time', 'customer_name', 'service_type']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'customer_name': forms.TextInput(attrs={'placeholder': 'Enter customer name...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer_name'].required = True