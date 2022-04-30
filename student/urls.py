from django.urls import path, include
from rest_framework import routers
from student.views import studentViewSet


app_name = 'student'

router = routers.SimpleRouter()
router.register('', studentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
