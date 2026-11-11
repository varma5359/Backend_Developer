from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("profile/<int:profile_id>/", views.profile_detail, name="profile_detail"),
    path("member/<str:username>/", views.member_detail, name="member_detail"),
    path("welcome/", views.welcome, name="welcome"),
    path("request-info/", views.request_info, name="request_info"),
    path("employee/", views.employee_demo, name="employee_demo"),
    path("students/", views.student_list, name="student_list"),
    path("students/register/", views.student_register, name="student_register"),
]
