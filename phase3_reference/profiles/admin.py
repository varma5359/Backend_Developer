from django.contrib import admin

from .models import Course, Department, Employee, Student, StudentProfile


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_code", "full_name", "email", "salary", "is_active")
    search_fields = ("employee_code", "full_name", "email")
    list_filter = ("is_active", "joining_date")
    ordering = ("full_name",)


admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentProfile)
