
from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Internship, StudentProfile
from .forms import InternshipForm, StudentProfileForm


# =========================
# Dashboard
# =========================

@login_required(login_url="/accounts/login/")
def dashboard(request):

    # Add a new internship application
    if request.method == "POST":

        form = InternshipForm(request.POST)

        if form.is_valid():

            internship = form.save(commit=False)
            internship.user = request.user
            internship.save()

            return redirect("dashboard")

    else:
        form = InternshipForm()

    # Get only the logged-in user's applications
    user_internships = Internship.objects.filter(
        user=request.user
    )

    # Search by company or role
    search = request.GET.get("search", "").strip()

    internships = user_internships

    if search:
        from django.db.models import Q

        internships = internships.filter(
            Q(company__icontains=search)
            | Q(role__icontains=search)
        )

    # Filter by application status
    status = request.GET.get("status", "").strip()

    if status:
        internships = internships.filter(status=status)

    # Dashboard statistics
    total_applications = user_internships.count()

    interview_count = user_internships.filter(
        status="Interview"
    ).count()

    selected_count = user_internships.filter(
        status="Selected"
    ).count()

    # Upcoming interviews: next five with a future or today's date
    upcoming_interviews = user_internships.filter(
        interview_date__gte=date.today(),
        status="Interview"
    ).order_by("interview_date")[:5]

    # Display dashboard
    return render(
        request,
        "index.html",
        {
            "internships": internships,
            "form": form,
            "total_applications": total_applications,
            "interview_count": interview_count,
            "selected_count": selected_count,
            "search": search,
            "selected_status": status,
            "upcoming_interviews": upcoming_interviews,
        }
    )


# =========================
# Edit Internship
# =========================

@login_required(login_url="/accounts/login/")
def edit_internship(request, id):

    internship = get_object_or_404(
        Internship,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = InternshipForm(
            request.POST,
            instance=internship
        )

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    else:
        form = InternshipForm(instance=internship)

    return render(
        request,
        "edit.html",
        {
            "form": form,
            "internship": internship,
        }
    )


# =========================
# Delete Internship
# =========================

@login_required(login_url="/accounts/login/")
def delete_internship(request, id):

    internship = get_object_or_404(
        Internship,
        id=id,
        user=request.user
    )

    internship.delete()

    return redirect("dashboard")


# =========================
# Student Profile and Resume
# =========================

@login_required(login_url="/accounts/login/")
def profile(request):

    student_profile, created = StudentProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        form = StudentProfileForm(
            request.POST,
            request.FILES,
            instance=student_profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = StudentProfileForm(instance=student_profile)

    return render(
        request,
        "profile.html",
        {
            "form": form,
        }
    )

