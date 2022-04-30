from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from course.models import Course
from course.serializers import CourseSerializer


class courseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer