# programs/filters.py
from django_filters import rest_framework as filters
from .models import Program


class ProgramFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="progrm_prc", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="progrm_prc", lookup_expr="lte")
    sido = filters.CharFilter(field_name="facility__sido__ctprvn_nm")
    days = filters.MultipleChoiceFilter(
        field_name="progrm_days", choices=Program.DAYS_CHOICES, conjoined=True
    )

    class Meta:
        model = Program
        fields = {
            "start_time": ["exact", "gte", "lte"],
            "end_time": ["exact", "gte", "lte"],
            "progrm_days": ["exact"],
        }
