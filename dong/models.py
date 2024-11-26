from django.db import models
from common.models import Common


# Create your models here.
class Dong(Common):
    sido = models.ForeignKey(
        "sido.Sido",
        on_delete=models.CASCADE,
        verbose_name="시도",
    )
    gugun = models.ForeignKey(
        "gugun.Gugun",
        on_delete=models.CASCADE,
        verbose_name="구군",
    )
    dong_name = models.CharField(
        max_length=20,
        verbose_name="동명",
    )

    class Meta:
        db_table = "dong"
        verbose_name = "동"
        verbose_name_plural = "동 목록"
        ordering = ["-created_at"]
