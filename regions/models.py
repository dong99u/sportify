# regions/models.py
from django.db import models
from common.models import Common


class Sido(Common):
    ctprvn_nm = models.CharField(max_length=20, verbose_name="시/도 이름")
    image = models.ImageField(
        upload_to="sido_images/", null=True, blank=True, verbose_name="시/도 이미지"
    )

    class Meta:
        db_table = "sido"
        verbose_name = "시/도"
        verbose_name_plural = "시/도 목록"

    def __str__(self):
        return self.ctprvn_nm


class Facility(Common):
    sido = models.ForeignKey(
        Sido, on_delete=models.CASCADE, related_name="facilities", verbose_name="시/도"
    )
    fclty_nm = models.CharField(max_length=100, verbose_name="시설 이름")
    fclty_addr = models.CharField(max_length=100, verbose_name="도로명 주소")

    class Meta:
        db_table = "facility"
        verbose_name = "시설"
        verbose_name_plural = "시설 목록"

    def __str__(self):
        return self.fclty_nm
