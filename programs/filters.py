from django_filters import rest_framework as filters
from .models import Program


class ProgramFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="progrm_prc", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="progrm_prc", lookup_expr="lte")
    sido = filters.CharFilter(field_name="facility__sido__ctprvn_nm")
    address = filters.CharFilter(
        field_name="facility__fclty_addr", lookup_expr="icontains"
    )
    days = filters.MultipleChoiceFilter(
        field_name="progrm_days", choices=Program.DAYS_CHOICES, conjoined=True
    )

    # 수강 기간 필터 추가
    begin_date = filters.DateFilter(field_name="progrm_begin_de", lookup_expr="gte")
    end_date = filters.DateFilter(field_name="progrm_end_de", lookup_expr="lte")

    class Meta:
        model = Program
        fields = {
            "start_time": ["exact", "gte", "lte"],
            "end_time": ["exact", "gte", "lte"],
            "progrm_days": ["exact"],
            "facility__fclty_addr": ["exact", "icontains"],
        }
