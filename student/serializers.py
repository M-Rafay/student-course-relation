from rest_framework import serializers
from student.models import Student
from course.models import Course

class StudentSerializer(serializers.ModelSerializer):
    """ Serializer for Student object """
    enrolled_courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all(), )

    class Meta:
        model = Student
        fields = ['id', 'name', 'enrolled_courses']
        read_only_fields = ['id']
        depth = 1
