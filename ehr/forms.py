from django import forms
from .models import Patient, Hospital, Doctor, Registration


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'