from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("forecaster.urls")),  # new
    path('upload/', include('forecaster.urls')),
]

