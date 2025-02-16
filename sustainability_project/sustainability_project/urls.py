from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("sustainability_app.urls")),  # Ensure only one "api/" prefix
]