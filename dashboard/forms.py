from django import forms
from .models import Internship, StudentProfile


class InternshipForm(forms.ModelForm):

    class Meta:
        model = Internship

        fields = [
            "company",
            "role",
            "application_date",
            "status",
            "interview_date",
            "notes",
        ]

        widgets = {
            "application_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "interview_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = [
    "full_name",
    "college",
    "branch",
    "graduation_year",
    "skills",
    "bio",
    "resume",
]

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your full name"
                }
            ),

            "college": forms.TextInput(
                attrs={
                    "placeholder": "Enter your college"
                }
            ),

            "branch": forms.TextInput(
                attrs={
                    "placeholder": "e.g. Information Technology"
                }
            ),

            "graduation_year": forms.NumberInput(
                attrs={
                    "placeholder": "e.g. 2028"
                }
            ),

            "skills": forms.Textarea(
                attrs={
                    "placeholder": "e.g. C++, Python, Django, HTML, CSS",
                    "rows": 4
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "placeholder": "Write a short introduction about yourself",
                    "rows": 5
                }
            ),
            "resume": forms.FileInput(
    attrs={
        "accept": ".pdf,.doc,.docx"
    }
),
        }