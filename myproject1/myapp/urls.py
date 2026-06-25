from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student),
    path('students/', views.course_students),
]