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
    image = models.ImageField(upload_to = 'media/') # This is an image field
    course_publish_date = models.DateTimeField(default=timezone.now) # This is a date time field
    course_type = models.CharField(max_length=4, choices=courseTypes) # This is a choice field
    course_description = models.TextField() # This is a text field