from django.urls import path, include
from rest_framework import routers
from course.views import courseViewSet


app_name = 'course'

router = routers.SimpleRouter()
router.register('', courseViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
