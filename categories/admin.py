from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "parent",
        "fclty_ty_nm",
        "get_description_preview",
        "created_at",
    ]
    list_filter = ["parent"]
    search_fields = ["fclty_ty_nm", "description"]
    autocomplete_fields = ["parent"]
    list_per_page = 20

    def get_description_preview(self, obj):
        return (
            obj.description[:50] + "..."
            if len(obj.description) > 50
            else obj.description
        )

    get_description_preview.short_description = "설명 미리보기"
