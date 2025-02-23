# Django
Django is a Python framework that makes it easier to create web sites using Python.

<font size="8">Install UV</font>
<!-- ## Install UV -->

UV is extermiliy fast Python package so that reason i install UV
``` terminal
pip install uv
```
## Create Virtal Environment with pip and uv
``` terminal
pip uv venv
```
## Virtal Environment Activate
```terminal
.venv\Script\activate
```
## Virtal Environment Deactivate
```terminal
dectivate
```
## Install Django
```terminal
uv pip install Django
```
## Start Project Start
```terminal
django-admin startproject DjangowithTomar
```
## Run Server 
```terminal
python manage.py runserver
```
## Run Server with specific port if not direct run on default port
```terminal
python manage.py runserver 80001
```
## Django Data flow
User => HTTP Response => URL Match in URL Router (url.py) => veiw function (views.py) => Render Template/JSON => model.py => Data Base

## Ready to Response 
after virtual environment go to views.py and import HttpResponse from django.http
```python
from django.http import HttpResponse

```

## Write function in views.py

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

# views import in urls.py
```python
from ./ import views
```

# urls handle in urls.py

```python
from ./ import views
urlpatterns = [
    path('', views.home, name='home')
    path('/about', views.about, name='about')
    path('/service', views.service, name='service')
    path('/contact', views.contact, name='contact')
]
```

# Run project 
```terminal
python manage.py runserver
```

# How to create Templates folder
under main project folder (root folder) you can create a folder to templates name for contain html files

# How to create static folder 
under main project folder (root folder) you can create a folder to static name for contain css, javascript files


# Which class import for data response to client web browser
```python
from django.http import HttpResponse

```

# Which function import for html files render 
```python
from django.shortcut import render 

# Example 01

def home(request):
    return render (request, 'index.html') 

# Example 02 : if files contain in folder like website
def about(request):
    return render (request, 'website/index.html')

```

# How to set in setting.py for new page load 
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
# How to link css with html in django
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
# How to seting (seting.py) static file directory file in django
```python
import os # import os library for 
from pathlib import Path

STATIC_URL = 'static/'
# Set this type path
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```


