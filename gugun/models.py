from django.db import models
from common.models import Common


# Create your models here.
class Gugun(Common):
    sido = models.ForeignKey(
        "sido.Sido",
        on_delete=models.CASCADE,
        verbose_name="시도",
    )

    gugun_name = models.CharField(
        max_length=20,
        verbose_name="구군명",
    )
