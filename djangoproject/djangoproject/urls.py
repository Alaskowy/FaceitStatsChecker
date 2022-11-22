from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path("api/", include("api.urls")),
    path("users/", include("users.urls")),
    path("dashboard/", include("dashboard.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
