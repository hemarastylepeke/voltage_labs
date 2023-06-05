from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to tailwind auto browser reload.
    path("__reload__/", include("django_browser_reload.urls")),

    # urls from main application.
    path("", include("main_app.urls")),

]

