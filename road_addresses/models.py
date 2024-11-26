from django.db import models
from common.models import Common


# Create your models here.
class RoadAddress(Common):
    dong = models.ForeignKey(
        "dong.Dong",
        on_delete=models.CASCADE,
        verbose_name="동",
    )
    road_name = models.CharField(
        max_length=20,
        verbose_name="로드명",
    )
    building_main_num = models.PositiveIntegerField(
        verbose_name="메인_building_num",
    )
    building_sub_num = models.PositiveIntegerField(
        verbose_name="부building_num",
    )
    building_name = models.CharField(
        max_length=20,
        verbose_name="building_name",
    )
    postal_code = models.CharField(
        max_length=5,
        verbose_name="우편번호코드",
    )

    class Meta:
        db_table = "road_address"
        verbose_name = "로드 주소"
        verbose_name_plural = "로드 주소 목록"
        ordering = ["-created_at"]
