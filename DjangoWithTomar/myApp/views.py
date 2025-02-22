from django.shortcuts import render

# Create your views here.
def first_Page(request):
    return render(request, 'myApp/first_Page.html')

