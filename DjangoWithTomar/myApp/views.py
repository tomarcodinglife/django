from django.shortcuts import render
from .models import Course

# Create your views here.

def myApp(request) :
    courses = Course.objects.all()
    # return render(request, 'myApp/index.html', {'courses': courses})
    return render(request, 'myApp/django.html', {'courses': courses})