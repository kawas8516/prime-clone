"""Root URL configuration for the prime project.

Author: kawas8516 <https://github.com/kawas8516>
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("content.urls")),
    path("", include("accounts.urls")),
]
