from django.http import HttpResponse

def home (request):
    return HttpResponse("Hi i am Sujit Tomar and that is Home Page")

def about (request):
    return HttpResponse("Hi i am Sujit Tomar and that is  about")

def contact (request):
    return HttpResponse("Hi i am Sujit Tomar and that is contact Page")