# Electronic Health Record (EHR) System

A practical web application built using Django to manage Electronic Health Records.This project supports CRUD (Create, Retrieve, Update, Delete) operations for managing Patients, Hospitals, Doctors, and Registrations through both the Django Admin panel and custom web views[cite: 109, 126].

---

## Table of Contents
1. [Features]
2. [Prerequisites]
3. [Installation & Setup]
4. [Database Migrations]
5. [Creating a Superuser]
6. [Project Structure]
7. [Running the Application]

---

## Features
Django Admin Integration: Easily manage core models (Hospitals, Doctors, Patients, and Registrations) with full CRUD permissions.
Web-Based Patient CRUD Views: Dedicated web interface to list, create, edit, and delete patient records.
Secure Forms: Built-in form validation and CSRF token protection for data handling.

## Prerequisites
Before running this project, ensure you have Python installed on your system. Familiarity with fundamental Python concepts (functions, classes, variables, and libraries) is highly recommended.

## Installation & Setup

Follow these step-by-step instructions to get your development environment running:

Step 1: Clone and Navigate to the Project Folder
git clone https://github.com/manishbhandari-tech/ehrproject.git
cd ehr_project

Step 2: Create and Activate a Virtual Environment
python -m venv env

Activate the virtual environment based on your operating system:

Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate

Step 3: Install Django
Install Django framework using pip: pip install django

(Optional) Check your installed Django version: django-admin --version

step 4: Create Django Project

django-admin startproject ehr_system
cd ehr_system

Run server:
python manage.py runserver
Open: http://127.0.0.1:8000/
CTRL + C to close the app

Step 5: Create EHR App
• python manage.py startapp ehr

Step 6: Register App in settings.py
Open: ehr_system/settings.py
Find INSTALLED_APPS and add:
'ehr',

Example:
INSTALLED_APPS = [
'ehr',
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
]

Step 7: Create Models
Open: ehr/models.py

• Write this code:
from django.db import models [cite: 47]

class Hospital(models.Model): [cite: 48]
    hospital_name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    established_date = models.DateField() 

    def __str__(self): 
        return self.hospital_name 

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100) 
    specialization = models.CharField(max_length=100) 
    phone = models.CharField(max_length=20) 
    email = models.EmailField() 
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE) 

    def __str__(self):
        return self.doctor_name 

class Patient(models.Model): 
    patient_name = models.CharField(max_length=100) 
    age = models.IntegerField() 
    gender = models.CharField(max_length=20) 
    address = models.CharField(max_length=255) 
    phone = models.CharField(max_length=20) 
    blood_group = models.CharField(max_length=10) 

    def __str__(self): 
        return self.patient_name 

class Registration(models.Model): 
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    registration_date = models.DateField(auto_now_add=True)
    symptoms = models.TextField() 
    diagnosis = models.TextField(blank=True, null=True) 

    def __str__(self): 
        return self.patient.patient_name 

Step 8: Create Migration
• python manage.py makemigrations

Expected output:
Create model Hospital
Create model Patient
Create model Doctor
Create model Registration

Step 9: Apply Migration
python manage.py migrate

This creates database tables.

Step 10: Register Models in Admin
Open: ehr/admin.py

Add:
from django.contrib import admin
from .models import Hospital, Doctor, Patient, 
Registration
admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Registration)

Step 11: Create Admin User
• python manage.py createsuperuser

Enter:
Username: admin
Email: admin@ehr.com
Password: ********

Step 12: Run Server
python manage.py runserver
Open: http://127.0.0.1:8000/admin/
Login using admin username and password

Add Data in Admin Panel
1. Add Hospital
2. Add Doctor
3. Add Patient
4. Add Registration

Final Output
You should see these models in Django Admin:
• Hospitals
• Doctors
• Patients
• Registrations

You should be able to:
• Add data
• Edit data
• Delete data

Model → Migration → Database Table → Admin Panel
• View stored records
