from django.urls import path
from .views import ProgramListAPIView

app_name = "programs"

urlpatterns = [
    path("", ProgramListAPIView.as_view(), name="program-list"),
]
