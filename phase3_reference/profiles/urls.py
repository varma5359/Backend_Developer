from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/register/", views.student_register, name="student_register"),
]
