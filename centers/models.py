from django.db import models
from common.models import Common


# Create your models here.
class SportsCenter(Common):

    road_address = models.ForeignKey(
        "road_addresses.RoadAddress",
        on_delete=models.CASCADE,
        verbose_name="ROAD ADDRESS",
    )

    center_name = models.CharField(
        max_length=255,
        verbose_name="SPORTS CENTER NAME",
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name="PHONE NUMBER",
    )

    class Meta:
        db_table = "sports_center"
        verbose_name = "스포츠 센터"
        verbose_name_plural = "스포츠 센터 목록"
        ordering = ["-created_at"]
