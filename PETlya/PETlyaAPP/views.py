from django.http import HttpResponse
from django.shortcuts import render
from .models import Appointment

def home(request):
    return render(request, 'index.html')

def appoint(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        pet_name = request.POST['petname']
        phone_number = request.POST['phone']
        problem = request.POST['illness']

        if len(name) is None:
            return HttpResponse('<h1>Error!<br>You dont write your name.</h1>')

        new_appointment = Appointment(name=name, surname=surname, pet_name=pet_name, phone_number=phone_number, problem=problem)
        new_appointment.save()

    return render(request, 'appointment.html')

