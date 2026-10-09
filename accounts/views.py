from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid username or password"
                }
            )

    return render(request, "login.html")


def logout_view(request):

    logout(request)

    return redirect("login")


def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check passwords
        if password != confirm_password:

            return render(
                request,
                "register.html",
                {
                    "error": "Passwords do not match"
                }
            )

        # Check username
        if User.objects.filter(username=username).exists():

            return render(
                request,
                "register.html",
                {
                    "error": "Username already exists"
                }
            )

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Login automatically
        login(request, user)

        return redirect("dashboard")

    return render(request, "register.html")