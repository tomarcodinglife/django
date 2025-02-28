from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hi i am learngin Django with Tomar That is Home Page")
    return render (request, 'website/index.html' )

def about(request):
    return HttpResponse("Hi i am learngin Django with Tomar That is about Page")

def service(request):
    return HttpResponse("Hi i am learngin Django with Tomar That is service Page")

def contact(request):
    return HttpResponse("Hi i am learngin Django with Tomar That is contact Page")

def career(request):  
    return HttpResponse("Hi i am learngin Django with Tomar That is career Page")