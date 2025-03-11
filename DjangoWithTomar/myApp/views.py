from django.shortcuts import render
from .models import Course
from django.shortcuts import get_object_or_404

# Create your views here.

def myApp(request) :
    courses = Course.objects.all()
    return render(request, 'myApp/home.html', {'courses': courses})

def course_details(request, course_id):
    course=get_object_or_404(Course, id=course_id)
    return render (request, 'myApp/course_detail.html', {'course': course})

# def course_detail(request, id):
#     course = Course.objects.get(id=id)
#     return render(request, 'myApp/course_detail.html', {'course': course})