from django.db import models
from common.models import Common


# Create your models here.
class JibunAddress(Common):
    dong = models.ForeignKey(
        "dong.Dong",
        on_delete=models.CASCADE,
        verbose_name="동",
    )
    main_num = models.PositiveIntegerField(
        verbose_name="메인 지번",
    )
    sub_num = models.PositiveIntegerField(
        verbose_name="부지번",
    )
    postal_code = models.CharField(
        max_length=5,
        verbose_name="우편번호코드",
    )
