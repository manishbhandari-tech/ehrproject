from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Hospital, Doctor, Registration
from .forms import PatientForm, HospitalForm, DoctorForm, RegistrationForm


def home(request):
    return render(request, "ehr/home.html")


# Patient CRUD


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, "ehr/patient_list.html", {"patients": patients})


def patient_create(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm()

    return render(request, "ehr/patient_form.html", {"form": form})


def patient_update(request, id):
    patient = get_object_for_404(Patient, id=id)

    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patient_list")
    else:
        form = PatientForm(instance=patient)

    return render(request, "ehr/patient_form.html", {"form": form})


def patient_delete(request, id):
    patient = get_object_for_404(Patient, id=id)

    if request.method == "POST":
        patient.delete()
        return redirect("patient_list")

    return render(request, "ehr/patient_confirm_delete.html", {"patient": patient})
