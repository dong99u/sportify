from django.db import models
from common.models import Common


# Create your models here.
class Sido(Common):
    sido_name = models.CharField(
        max_length=20,
        verbose_name="시도명",
    )

    class Meta:
        db_table = "sido"
        verbose_name = "시도"
        verbose_name_plural = "시도 목록"
        ordering = ["-created_at"]
