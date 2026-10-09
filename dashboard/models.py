from django.db import models
from django.contrib.auth.models import User


class Internship(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    company = models.CharField(
        max_length=100
    )

    role = models.CharField(
        max_length=100
    )

    application_date = models.DateField()

    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Assessment", "Assessment"),
        ("Interview", "Interview"),
        ("Selected", "Selected"),
        ("Rejected", "Rejected"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applied"
    )

    interview_date = models.DateField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.company} - {self.role}"


class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    full_name = models.CharField(
        max_length=100,
        blank=True
    )

    college = models.CharField(
        max_length=150,
        blank=True
    )

    branch = models.CharField(
        max_length=100,
        blank=True
    )

    graduation_year = models.IntegerField(
        null=True,
        blank=True
    )

    skills = models.TextField(
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.user.username