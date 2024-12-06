from django_filters import rest_framework as filters
from .models import Program
from django.db.models import Q

class ProgramFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='progrm_prc', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='progrm_prc', lookup_expr='lte')
    sido = filters.CharFilter(field_name='facility__sido__ctprvn_nm')
    days = filters.MultipleChoiceFilter(
        field_name='progrm_days',
        choices=Program.DAYS_CHOICES,
        conjoined=True
    )
    
    progrm_begin_de = filters.DateFilter(method='filter_program_date')
    progrm_end_de = filters.DateFilter(method='filter_program_date')

    def filter_program_date(self, queryset, name, value):
        """
        프로그램 시작일과 종료일이 지정된 기간 내에 있는지 확인
        """
        if name == 'progrm_begin_de':
            # 프로그램 시작일이 지정된 날짜 이후인 경우만 필터링
            return queryset.filter(progrm_begin_de__gte=value)
        elif name == 'progrm_end_de':
            # 프로그램 종료일이 지정된 날짜 이전인 경우만 필터링
            return queryset.filter(progrm_end_de__lte=value)
        return queryset

    class Meta:
        model = Program
        fields = {
            'start_time': ['exact', 'gte', 'lte'],
            'end_time': ['exact', 'gte', 'lte'],
            'progrm_days': ['exact'],
            'facility__sido': ['exact'],
        }
