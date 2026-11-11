from django.shortcuts import redirect, render

from .forms import StudentRegistrationForm
from .models import Student


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
