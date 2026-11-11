from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import StudentRegistrationForm
from .models import Student


def home(request):
    return render(request, "profiles/home.html")


def about(request):
    return render(request, "profiles/about.html")


def profile_detail(request, profile_id):
    return HttpResponse(f"Profile ID: {profile_id}")


def member_detail(request, username):
    return HttpResponse(f"Member: {username}")


def welcome(request):
    name = request.GET.get("name", "Guest")
    return render(request, "profiles/welcome.html", {"name": name})


def request_info(request):
    return HttpResponse(f"Method: {request.method}")


def employee_demo(request):
    employee = {
        "name": "Asha Rao",
        "role": "Backend Developer",
        "skills": ["Python", "Django", "SQL"],
    }
    return render(
        request,
        "profiles/employee_profile.html",
        {"employee": employee},
    )


def student_list(request):
    students = Student.objects.order_by("full_name")
    return render(
        request,
        "profiles/student_list.html",
        {"students": students},
    )


def student_register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "profiles/student_form.html",
        {"form": form},
    )
