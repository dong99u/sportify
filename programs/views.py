from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Program
from .serializers import ProgramSerializer
from .filters import ProgramFilter


class ProgramListAPIView(generics.ListAPIView):
    queryset = Program.objects.select_related(
        "category",
        "facility",
        "facility__sido",  # sido 정보를 가져오기 위한 select_related
    ).all()
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProgramFilter
    search_fields = ["progrm_nm", "facility__fclty_nm", "category__fclty_ty_nm"]
    ordering_fields = ["progrm_prc", "start_time", "created_at"]
    ordering = ["start_time"]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        return context
