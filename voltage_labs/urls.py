from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, include, re_path


urlpatterns = [
    # Path for admin page
    path('admin/', admin.site.urls),

    # Path to tailwind auto browser reload.
    path("__reload__/", include("django_browser_reload.urls")),

    # urls from main application.
    path("", include("main_app.urls")),

    # path to handle media files in production.
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

