from django.urls import path
from . import views

urlpatterns = [
    path('', views.myApp, name = 'myApp Home Page'),
    path('<int:course_id>/', views.course_detail, name = 'course_detail'),
]
