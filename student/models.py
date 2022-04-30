from django.db import models
from course.models import Course
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255, unique=True)
    enrolled_courses = models.ManyToManyField(Course, related_name='student_courses')    
    
    def __str__(self):
        return self.name