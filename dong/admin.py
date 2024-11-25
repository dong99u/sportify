from django.contrib import admin
from .models import Dong


@admin.register(Dong)
class DongAdmin(admin.ModelAdmin):
    list_display = [
        "dong_name",
        "get_sido_name",
        "get_gugun_name",
        "created_at",
        "updated_at",
    ]

    list_filter = [
        "sido",
        "gugun",
    ]

    search_fields = [
        "dong_name",
        "sido__sido_name",
        "gugun__gugun_name",
    ]

    readonly_fields = ["created_at", "updated_at"]

    def get_sido_name(self, obj):
        return obj.sido.sido_name if obj.sido else "-"

    get_sido_name.short_description = "시도"

    def get_gugun_name(self, obj):
        return obj.gugun.gugun_name if obj.gugun else "-"

    get_gugun_name.short_description = "구군"
