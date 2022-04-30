from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from student.models import Student
from student.serializers import StudentSerializer


class studentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
