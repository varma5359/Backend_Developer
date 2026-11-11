from django import forms
from .models import Student


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["student_code", "full_name", "email"]

    def clean_student_code(self):
        code = self.cleaned_data["student_code"].strip().upper()
        if not code.startswith("STU"):
            raise forms.ValidationError("Student code must start with STU.")
        return code

    def clean(self):
        cleaned_data = super().clean()
        full_name = cleaned_data.get("full_name")
        email = cleaned_data.get("email")

        if full_name and email and full_name.casefold() in email.casefold():
            self.add_error(
                "email",
                "Email should not contain the full student name.",
            )
        return cleaned_data
