from django.contrib import admin
from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "progrm_nm",
        "get_category",
        "get_facility",
        "get_days_display",
        "get_time_display",
        "progrm_begin_de",
        "progrm_end_de",
        "progrm_prc",
        "progrm_rcrit_nmpr_co",
    ]
    list_filter = [
        "category",
        "facility",
        "progrm_days",
        "start_time",
        "progrm_begin_de",
        "progrm_end_de",
    ]
    search_fields = ["progrm_nm", "category__fclty_ty_nm", "facility__fclty_nm"]
    autocomplete_fields = ["category", "facility"]
    readonly_fields = ["created_at", "updated_at"]
    list_per_page = 20

    def get_category(self, obj):
        return obj.category.fclty_ty_nm

    get_category.short_description = "종목"

    def get_facility(self, obj):
        return obj.facility.fclty_nm

    get_facility.short_description = "시설"

    def get_days_display(self, obj):
        return obj.get_days_display_korean

    get_days_display.short_description = "운영 요일"

    def get_time_display(self, obj):
        return obj.get_time_range

    get_time_display.short_description = "운영 시간"

    fieldsets = (
        ("기본 정보", {"fields": ("progrm_nm", "category", "facility", "hmpg_url")}),
        (
            "운영 정보",
            {
                "fields": (
                    "progrm_days",
                    ("start_time", "end_time"),
                    "progrm_begin_de",
                    "progrm_end_de",
                )
            },
        ),
        (
            "수강 정보",
            {"fields": ("progrm_prc", "progrm_rcrit_nmpr_co", "progrm_trget_nm")},
        ),
        (
            "시스템 정보",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
