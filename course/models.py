from django.db import models

# Create your models here.

class Course(models.Model):
    course_name  = models.CharField(max_length=255, unique=True)
    source  = models.CharField(max_length=255)
    
    def __str__(self):
        return self.course_name