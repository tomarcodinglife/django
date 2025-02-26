from django .http import HttpResponse
from django .shortcuts import render

def home(request) :
    # return HttpResponse("Hello Django, You are one of the best Framework of python - Home Page")
    return render(request, 'website/index.html')

def about(request) :
    return HttpResponse("Hello Django, You are one of the best Framework of python - about Page")

def contact(request) :
    return HttpResponse("Hello Django, You are one of the best Framework of python - contact Page")

def root(request) :
    return render(request, 'website/root.html')