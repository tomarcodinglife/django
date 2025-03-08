from django.db import models
from django.utils import timezone
# Create your models here.
class Course(models.Model): # This is a model class
    Required_Language = [             # This is a list of tuples
        ('JS', 'Javascript'),
        ('PY', 'Python'),
        ('CPP', 'C++'),
        ('C#', 'C Sharp'),
        ('Java', 'Java'),
        ('DB', 'Database'),
    ]
    course_Name = models.CharField(max_length=30) # This is a char field
    thumbnails = models.ImageField(upload_to = 'media/') # This is an image field
    course_publish_date = models.DateTimeField(default=timezone.now) # This is a date time field
    Language_Required = models.CharField(max_length=4, choices=Required_Language) # This is a choice field
    Course_Description = models.TextField() # This is a text field

# it is used to display the name of the course in the admin panel
    def __str__(self):
        return self.course_Name
