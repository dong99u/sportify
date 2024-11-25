from django.db import models
from common.models import Common


# Create your models here.
class Sido(Common):
    sido_name = models.CharField(
        max_length=20,
        verbose_name="시도명",
    )
