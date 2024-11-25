from django.contrib import admin
from .models import Gugun


@admin.register(Gugun)
class GugunAdmin(admin.ModelAdmin):
    list_display = [
        "gugun_name",
        "get_sido_name",
        "created_at",
        "updated_at",
    ]

    list_filter = ["sido"]

    search_fields = [
        "gugun_name",
        "sido__sido_name",
    ]

    readonly_fields = ["created_at", "updated_at"]

    def get_sido_name(self, obj):
        return obj.sido.sido_name if obj.sido else "-"

    get_sido_name.short_description = "시도"
