from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def signupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return render(
                request, "signup.html", {"error": "Username and password are required."}
            )

        if User.objects.filter(username=username).exists():
            return render(
                request, "signup.html", {"error": "That username is already taken."}
            )

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
