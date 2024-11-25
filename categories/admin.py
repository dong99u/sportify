from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_name", "parent", "get_full_category_path"]
    list_filter = ["parent"]
    search_fields = ["name", "category_name", "description"]
    ordering = ["name"]

    # 계층 구조를 보여주기 위한 들여쓰기
    def get_full_category_path(self, obj):
        return obj.get_full_category_path()

    get_full_category_path.short_description = "전체 경로"
