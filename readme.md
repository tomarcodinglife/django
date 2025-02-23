# Django
Django is a Python framework that makes it easier to create web sites using Python.

## Install UV
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

