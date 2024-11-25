# courses/models.py
from django.db import models
from common.models import Common

class Category(Common):
    parent = models.ForeignKey(
        "self", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='children',
        verbose_name='상위 종목'
    )
    name = models.CharField(
        max_length=255,
        verbose_name='카테고리명'
    )
    category_name = models.CharField(
        max_length=255, 
        verbose_name='종목명'
    )
    description = models.TextField(
        verbose_name='설명',
        help_text='종목에 대한 상세 설명을 입력하세요'
    )

    class Meta:
        db_table = "category"
        verbose_name = "종목"
        verbose_name_plural = "종목 목록"
        ordering = ['name']

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} > {self.name}"
        return self.name

    def get_full_category_path(self):
        """카테고리의 전체 경로를 반환"""
        if self.parent:
            return f"{self.parent.get_full_category_path()} > {self.name}"
        return self.name

    def get_all_children(self):
        """모든 하위 카테고리를 반환"""
        return self.children.all()

    def get_siblings(self):
        """같은 레벨의 다른 카테고리들을 반환"""
        if self.parent:
            return self.parent.children.exclude(id=self.id)
        return Category.objects.filter(parent=None).exclude(id=self.id)

    @property
    def has_children(self):
        """하위 카테고리가 있는지 확인"""
        return self.children.exists()

    @property
    def level(self):
        """카테고리의 깊이 레벨을 반환"""
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level