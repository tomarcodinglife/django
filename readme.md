# Django
Django is a Python framework that makes it easier to create web sites using Python.

<h3>Install UV</h3>
<!-- ## Install UV -->
UV is extermiliy fast Python package so that reason i install UV
``` terminal
pip install uv
```
<!-- .......................................................................... -->
<h3>Create Virtal Environment with pip and uv</h3>
``` terminal
pip uv venv
```
<!-- .......................................................................... -->
<h3>Virtual Environment Activate</h3>
```terminal
.venv\Script\activate
```
<!-- .......................................................................... -->
<h3>Virtual Environment Deactivate</h3>
```terminal
dectivate
```
<!-- .......................................................................... -->
<h3>Install Django</h3>
```terminal
uv pip install Django
```
<!-- .......................................................................... -->
<h3>Start Project Start</h3>
```terminal
django-admin startproject DjangowithTomar
```
<!-- .......................................................................... -->
<h3>Run Server</h3>
```terminal
python manage.py runserver
```
<!-- .......................................................................... -->
<h3>Run Server with specific port if not direct run on default port<h3> 
```terminal
python manage.py runserver 80001
```
<!-- .......................................................................... -->
<h3>Django Data flow</h3>
User => HTTP Response => URL Match in URL Router (url.py) => veiw function (views.py) => Render Template/JSON => model.py => Data Base

<!-- .......................................................................... -->
<h3>Ready to Response</h3>

after virtual environment go to views.py and import HttpResponse from django.http
```python
from django.http import HttpResponse

```
<!-- .......................................................................... -->
<h3>Write function in views.py</h3>

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi This is Home Page")

def about(request):
    return HttpResponse("Hi This is about Page")

def service(request):
    return HttpResponse("Hi This is service Page")

def contact(request):
    return HttpResponse("Hi This is contact Page")
```
<!-- .......................................................................... -->
<h3>views import in urls.py</h3>

```python
from ./ import views
```
<!-- .......................................................................... -->
<h3>urls handle in urls.py</h3>

```python
from ./ import views
urlpatterns = [
    path('', views.home, name='home')
    path('/about', views.about, name='about')
    path('/service', views.service, name='service')
    path('/contact', views.contact, name='contact')
]
```
<!-- .......................................................................... -->
<h3>Run project</h3>

```terminal
python manage.py runserver
```
<!-- .......................................................................... -->
<h3>How to create Templates folder</h3>

under main project folder (root folder) you can create a folder to templates name for contain html files

<!-- .......................................................................... -->

<h3>How to create static folder </h3>
under main project folder (root folder) you can create a folder to static name for contain css, javascript files

<!-- .......................................................................... -->

<h3>Which class import for data response to client web browser</h3>

```python
from django.http import HttpResponse

```
<!-- .......................................................................... -->

<h3>Which function import for html files render</h3>

```python
from django.shortcut import render 

# Example 01

def home(request):
    return render (request, 'index.html') 

# Example 02 : if files contain in folder like website
def about(request):
    return render (request, 'website/index.html')

```
<!-- .......................................................................... -->

<h3>How to set in setting.py for new page load</h3>

```python
# in templates section by default look like this 
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# in DIRS you put file name templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # its mandatory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
<!-- .......................................................................... -->
<h3>How to link css with html in django</h3>

```html
{% load static %}  <!--Load static engine -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Django</title>
    <!--CSS inject in html like that -->
    <link rel="stylesheet" href="{% static 'style.css' %}"> 
</head>
<body>
    <h1>Django with Tomar</h1>
</body>
</html>
```
<!-- .......................................................................... -->
<h3>How to seting (seting.py) static file directory file in django</h3>
```python
import os # import os library for 
from pathlib import Path

STATIC_URL = 'static/'
# Set this type path
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```


