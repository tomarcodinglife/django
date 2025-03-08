# Django
Django is a Python framework that makes it easier to create web sites using Python.

<h2>Installation Section</h2>

<!-- .......................................................................... -->

<h3>Create Virtal Environment with python </h3>

``` terminal
py -m venv .venv
```

<!-- .......................................................................... -->

<h3>You can pip update </h3>

```terminal
py -m pip install --upgrade pip
py -m pip --version
```

<!-- .......................................................................... -->

<h3>Virtual Environment Activate</h3>

```terminal
.venv\Scripts\activate
```

<!-- .......................................................................... -->

<h3>Virtual Environment Deactivate</h3>

```terminal
dectivate
```
<!-- .......................................................................... -->
<h3>Install Django</h3>

```terminal
py -m pip install Django
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
<h3>Run Server with specific port if not direct run on default port</h3> 

```terminal
python manage.py runserver 80001
```

<!-- .......................................................................... -->

<h2>Data Flow Section</h2>

<!-- .......................................................................... -->

<h3>Django Data flow</h3>
User => HTTP Response => URL Match in URL Router (url.py) => veiw function (views.py) => Render Template/JSON => model.py => Data Base

<h2>Directory Section</h2>

<!-- .......................................................................... -->
<h3>Make Ready to Response file</h3>

after virtual environment create a folder views.py and import HttpResponse from django.http

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
<h3>Create Templates folder</h3>

under main project folder (root folder) you can create a folder to templates name for contain html files

<!-- .......................................................................... -->

<h3>Create static folder </h3>
under main project folder (root folder) you can create a folder to static name for contain css, javascript files

<!-- .......................................................................... -->

<h3>Class import for data response to client web browser</h3>

```python

from django.http import HttpResponse

```
<!-- .......................................................................... -->

<h3>Function import for html files render</h3>

```python

from django.shortcut import render 

# Example 01

def home(request):
    return render (request, 'index.html') # if the html file name are index.html

# Example 02 : if files contain in folder like website
def about(request):
    return render (request, 'website/index.html') 

```
<!-- .......................................................................... -->

<h3>Set in setting.py for new page load</h3>

```python
# in DIRS you put file name templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # its mandatory to render templates files
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
<h3>Link css with html in django</h3>

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
<h3>CSS Files Setup in Django Section</h3>
<!-- .......................................................................... -->
<h3>Setting (setting.py) static file directory file in django</h3>

```python

import os # import os library for 
from pathlib import Path

STATIC_URL = 'static/'
# Set this type path
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```
<!-- .......................................................................... -->
<h2>App Section </h2>
<!-- .......................................................................... -->
<h3>Create apps folder in django</h3>
<p>first of all go to root folder where you can see manage.py file by terminal ls command after that run command</p>

```terminal
python manage.py startapp myApp
```
<!-- .......................................................................... -->
<h3>Aware my new app folder in django </h3>
<p>Go to settings.py file where you see by default installed apps you join the new app name that you create like myApp</p>

```python

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
]

```
<!-- .......................................................................... -->
<h3>Create templates folder for New App (like myApp) as per required</h3>
<p>you can use templates folder which is already exist in root directory or you can create a folder under new app (like - myApp)<p>
<img src="https://github.com/tomarcodinglife/Data_File/blob/main/imageData/File_Directory_for_Django.png" alt="" height="500px" title="Directory">

<!-- .......................................................................... -->

<h3>Add django html for suggestion (emmet) for new app </h3>

<p> press (ctrl + ,) => go to Emmet include Language and set in item section django-html and in value section html</p>

<img src="https://github.com/tomarcodinglife/Data_File/blob/main/imageData/django-html_set_in_emmet_language.png" alt="" height="300px" title="set emmet language">

<!-- .......................................................................... -->

<h3>Create files under templates under new app  (like - myApp) </h3>

<img src="https://github.com/tomarcodinglife/Data_File/blob/main/imageData/Django_myApp_templates_under_create_files.gif" alt="" height="400px" title="Create html Files under Django App templates">

<!-- .......................................................................... -->

<h3>Control transfer root file urls.py to under new app urls.py (like - myApp)</h3>

<img src="https://github.com/tomarcodinglife/Data_File/blob/main/imageData/my_app_urls_views_setup.gif" alt="" height="400px" title="myApp connect urls.py to main file's urls.py">


<!-- .......................................................................... -->
<h2> Tailwind with Django Section </h2>
<!-- .......................................................................... -->

<h3>Install tailwind</h3>

<p> first you should know that tailwind install in Django without error with pip so please check your pip working or not if not working then install again with following two command but use any one command.</p>

<h4> First Command </h4>

```terminal
python -m pip install --upgrade pip
```

<h4> Second Command </h4> 

```terminal
python -m ensurepip --upgrade
```

<!-- .......................................................................... -->

<h3>Download tailwind with Django using Command</h3> 

```terminal
pip install django-tailwind
```

<!-- .......................................................................... -->


<h3>tailwind with Django reload Command</h3> 

```terminal
pip install 'django-tailwind[reload]'
```

<!-- .......................................................................... -->

<h3> How to add tailwind in root folder's setting.py </h3>

<img src="https://github.com/tomarcodinglife/Data_File/blob/main/imageData/tailwind_app_add_in_setting.py_file.png" alt="" height="400px" title="tailwind app add in root folder's setting.py">

<!-- .......................................................................... -->

<h3> Start server with tailwind after install tailwind </h3>
<p> Run that command under root folder where manage.py available</p>

```terminal
python manage.py tailwind init
```

<!-- .......................................................................... -->

<h3>Set tailwind in root folder's file setting.py</h3>

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
    'tailwind', # add it manualy in setting.py of root folder
]
 # add that ip because now you have two server after tailwind install

```

<!-- .......................................................................... -->

<!-- <img src="https://github.com/tomarcodinglife/Data_File/blob/main/imageData/tailwind_setting_under_setting.py_of_root_folder.png" alt="" height="400px" title="tailwind setting in root folder's setting.py"> -->


<!-- .......................................................................... -->

<h3> Install tailwind after download and setup mandatory settings in setting.py </h3>

```terminal
python manage.py tailwind install
```

<!-- .......................................................................... -->

<h3>Set tailwind theme in root folder's file setting.py</h3>

```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myApp',
    'tailwind', # add it manualy in setting.py of root folder
    'theme',    # add it as per your theme name (default i lkie theme like that)
]

TAILWIND_APP_NAME = 'theme' #add that after theme folder create if your theme folder name theme
INTERNAL_IPS = ['127.0.0.1']

NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd" # it add as per own system npm location

 # add that ip because now you have two server after tailwind install

```

<!-- .......................................................................... -->

<h3> After Install tailwind its html file look like that under theme folder</h3>

<img src="https://raw.githubusercontent.com/tomarcodinglife/Data_File/refs/heads/main/imageData/tailwind_html_file_under_django_theme_after_tailwind_installation.png" alt="" height="400px" title="tailwind theme ">

<!-- .......................................................................... -->

<h3> After Install tailwind you can use tailwind css under own app look like that</h3>

<img src="https://raw.githubusercontent.com/tomarcodinglife/Data_File/refs/heads/main/imageData/after_install_tailwind_you_add_tailwind_css_under_own_app_html_files.png" alt="" height="400px" title="tailwind theme">

<!-- .......................................................................... -->

<h2>Webpage or Web browser automatically reload section</h2>

<!-- .......................................................................... -->

<h3>reload webpage or web browser automatically</h3>
<p>Now you want reload webpage or web browser automatically for both tailwind and django so In this case you will have to use a separate terminal for Tailwind css and a separate terminal for Django. As shown in the picture above</p>

<h3>Run command for django auto reload page </h3>

<p> First Run this command in seprate terminal </p>

```terminal
python -m pip install django-browser-reload
```

<p> Ensure you have "django.contrib.staticfiles" in your INSTALLED_APPS </p>

<p> Add django-browser-reload to your INSTALLED_APPS </p>

```python
INSTALLED_APPS = [
    ...,
    "django_browser_reload",
    ...,
]
```
<p> Include the app URLs in your root URLconf </p>

```python
from django.urls import include, path

urlpatterns = [
    ...,

    path("__reload__/", include("django_browser_reload.urls")),
]
```
<p> Add the middleware </p>

```python
MIDDLEWARE = [
    # ...
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    # ...
]
```

<p> After that run separate terminal (its tailwind updated automatically) </p>

```terminal
python manage.py runserver 
```

<p> After that run separate terminal (its virtual environment reload automatically) </p>

```terminal
.venv/Scripts/activate
```

<h3>If you want to migrate properly files</h3>

```terminal
python manage.py migrate
```

<h3>after that you run server properly</h3>

```terminal
python manage.py runserver
```

<h3>After migrate properly you go to admin page</h3>
<p> After migrate and runserver you can see (server run ip/admin) page </p>




<h3> Create Super user for acess admin page </h3>

```terminal
python manage.py createsuperuser
```
<p> After that set username its mandatory and email is optional and set password with special character and character should be more than 8 character after that you can login admin page using credentials </p>



<h3>Change Password for admin page</h3>

```terminal
python manage.py changepassword username
```
<p> After that set password with special character and character should be more than 8 character after that you can login admin page using credentials</p>


<h2>models (models.py) Section</h2>

<h3>write models (models.py) as per your need</h3>
<p>Now you can write models (models.py) in own created apps as per your nee like bellow mention</p>

```python

from django.db import models
from django.utils import timezone
# Create your models here.
class courseType(models.Model): # This is a model class
    courseTypes = [             # This is a list of tuples
        ('JS', 'Javascript'),
        ('PY', 'Python'),
        ('CPP', 'C++'),
        ('C#', 'C Sharp'),
        ('Java', 'Java'),
        ('DB', 'Database'),
    ]
    course_name = models.CharField(max_length=30) # This is a char field
    image = models.ImageField(upload_to = 'images/') # This is an image field
    course_publish_date = models.DateTimeField(default=timezone.now) # This is a date time field
    course_type = models.CharField(max_length=4, choices=courseTypes) # This is a choice field
    course_description = models.TextField() # This is a text field

```

<h3>Now handle Image with install pillow</h3>

```terminal

python -m pip install Pillow

```