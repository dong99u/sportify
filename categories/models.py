from django.db import models
from common.models import Common


class Category(Common):
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="상위 카테고리",
    )
    fclty_ty_nm = models.CharField(max_length=100, verbose_name="시설 유형명")
    description = models.TextField(verbose_name="설명")

    class Meta:
        db_table = "category"
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"

    def __str__(self):
        return self.fclty_ty_nm
