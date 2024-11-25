from django.db import models
from common.models import Common


# Create your models here.
class SportsCenter(Common):

    road_address = models.ForeignKey(
        "road_addresses.RoadAddress",
        on_delete=models.CASCADE,
        verbose_name="ROAD ADDRESS",
    )
    jibun_address = models.ForeignKey(
        "jibun_addresses.JibunAddress",
        on_delete=models.CASCADE,
        verbose_name="JIBUN ADDRESS",
    )
    center_name = models.CharField(
        max_length=255,
        verbose_name="SPORTS CENTER NAME",
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name="PHONE NUMBER",
    )
