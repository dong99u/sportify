from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/programs/", include("programs.urls")),  # programs.urls를 include
    path("api-auth/", include("rest_framework.urls")),
    path("", include("common.urls")),  # health check URL 추가
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
