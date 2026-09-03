"""URL routes for signup, login and logout.

Author: kawas8516 <https://github.com/kawas8516>
"""

from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("signup/", views.signupPage, name="signup"),
    path("logout/", views.logoutPage, name="logout"),
]
