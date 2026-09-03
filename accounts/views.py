"""Signup, login and logout views.

Author: kawas8516 <https://github.com/kawas8516>
"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render


def signupPage(request):
    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        password = request.POST.get("password") or ""

        def reject(error):
            # Keep the username so the user does not retype it.
            return render(
                request, "signup.html", {"error": error, "username": username}
            )

        if not username or not password:
            return reject("Username and password are required.")

        if User.objects.filter(username=username).exists():
            return reject("That username is already taken.")

        # create_user() hashes the password but does not run
        # AUTH_PASSWORD_VALIDATORS, so enforce them here.
        try:
            validate_password(password, User(username=username))
        except ValidationError as exc:
            return reject(" ".join(exc.messages))

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("home")

    return render(request, "signup.html")


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(
                request, "login.html", {"error": "Invalid username or password."}
            )

        login(request, user)
        return redirect("home")

    return render(request, "login.html")


def logoutPage(request):
    logout(request)
    return redirect("login")
