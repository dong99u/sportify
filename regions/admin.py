from django.contrib import admin
from .models import Sido, Facility


@admin.register(Sido)
class SidoAdmin(admin.ModelAdmin):
    list_display = ["id", "ctprvn_nm", "get_image_preview", "created_at", "updated_at"]
    search_fields = ["ctprvn_nm"]
    list_per_page = 20

    def get_image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return "-"

    get_image_preview.short_description = "이미지"
    get_image_preview.allow_tags = True


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ["id", "sido", "fclty_nm", "fclty_addr", "created_at"]
    list_filter = ["sido"]
    search_fields = ["fclty_nm", "fclty_addr"]
    autocomplete_fields = ["sido"]
    list_per_page = 20
