from django.db import models

from common.models import Common
from multiselectfield import MultiSelectField
from datetime import time


class Program(Common):
    DAYS_CHOICES = [
        ("MON", "월"),
        ("TUE", "화"),
        ("WED", "수"),
        ("THU", "목"),
        ("FRI", "금"),
        ("SAT", "토"),
        ("SUN", "일"),
    ]

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="카테고리",
    )
    facility = models.ForeignKey(
        "regions.Facility",
        on_delete=models.CASCADE,
        related_name="programs",
        verbose_name="시설",
    )
    progrm_nm = models.CharField(max_length=100, verbose_name="프로그램명")
    hmpg_url = models.CharField(max_length=100, verbose_name="홈페이지 URL")

    progrm_days = MultiSelectField(
        choices=DAYS_CHOICES,
        max_choices=7,
        max_length=100,
        verbose_name="운영 요일",
        default=["MON"],
    )

    start_time = models.TimeField(verbose_name="시작 시간", default=time(9, 0))  # 09:00
    end_time = models.TimeField(verbose_name="종료 시간", default=time(9, 50))  # 09:50

    progrm_begin_de = models.DateField(verbose_name="시작일")
    progrm_end_de = models.DateField(verbose_name="종료일")
    progrm_prc = models.IntegerField(verbose_name="수강료")
    progrm_rcrit_nmpr_co = models.IntegerField(verbose_name="모집인원")
    progrm_trget_nm = models.CharField(max_length=30, verbose_name="대상")

    class Meta:
        db_table = "program"
        verbose_name = "프로그램"
        verbose_name_plural = "프로그램 목록"
        ordering = ["start_time"]

    def __str__(self):
        return self.progrm_nm

    @property
    def get_days_display_korean(self):
        """요일을 한글로 변환하여 반환"""
        days_dict = dict(self.DAYS_CHOICES)
        return ", ".join(days_dict[day] for day in self.progrm_days)

    @property
    def get_time_range(self):
        """시간 범위를 문자열로 반환"""
        return (
            f'{self.start_time.strftime("%H:%M")} ~ {self.end_time.strftime("%H:%M")}'
        )
