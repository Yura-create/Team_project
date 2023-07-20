from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Appointment

def home(request):
    return render(request, 'index.html', {'title': 'PETlya'})

def home_ua(request):
    return render(request, 'index_ua.html', {'title': 'PETlya'})

def success(request):
    return render(request, 'success.html')


def check_app(request):
    appointments = Appointment.objects.all()
    return render(request, 'check_app.html', {'appointments': appointments})

def appoint(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        pet_name = request.POST['petname']
        phone_number = request.POST['phone']
        problem = request.POST['illness']

        if len(pet_name) < 1:
            return HttpResponse('<h1>Error! You forget to write something.</h1>')
        else:
            new_appointment = Appointment(name=name, surname=surname, pet_name=pet_name, phone_number=phone_number, problem=problem)
            new_appointment.save()
            return redirect(success)

    return render(request, 'appointment.html', {'title': 'Appointment'})

