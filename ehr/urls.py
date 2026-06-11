from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/update/<int:id>/', views.patient_update,
name='patient_update'),
    path('patients/delete/<int:id>/', views.patient_delete,
name='patient_delete'),
]