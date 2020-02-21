from django.shortcuts import render
from .models import *

def patient(request):

    patients = Patient.objects.all()

    return render(request, 'patients/views/patient_list.html', {'patients' : patients})


def patient_dashboard(request):

    # patients = Patient.object.all()

    return render(request, 'patients/views/patient_dashboard.html', {})
