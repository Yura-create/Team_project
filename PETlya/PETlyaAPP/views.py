from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def appoint(request):
    return render(request, 'appointment.html')
