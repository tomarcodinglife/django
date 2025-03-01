from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    # return HttpResponse("Hi i am Sujit Tomar and that is Home Page")
    return render(request, 'website/index.html')

def about (request):
    return HttpResponse("Hi i am Sujit Tomar and that is  about")

def contact (request):
    return HttpResponse("Hi i am Sujit Tomar and that is contact Page")