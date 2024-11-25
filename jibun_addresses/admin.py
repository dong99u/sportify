from django.contrib import admin
from .models import JibunAddress


@admin.register(JibunAddress)
class JibunAddressAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_address",
        "postal_code",
        "get_sido_name",
        "get_gugun_name",
        "get_dong_name",
        "main_num",
        "sub_num",
    ]

    list_filter = [
        "dong__sido",
        "dong__gugun",
        "dong",
    ]

    search_fields = [
        "postal_code",
        "dong__dong_name",
        "dong__gugun__gugun_name",
        "dong__sido__sido_name",
        "main_num",
        "sub_num",
    ]

    readonly_fields = ["created_at", "updated_at"]

    def get_sido_name(self, obj):
        return obj.dong.sido.sido_name if obj.dong and obj.dong.sido else "-"

    get_sido_name.short_description = "시도"

    def get_gugun_name(self, obj):
        return obj.dong.gugun.gugun_name if obj.dong and obj.dong.gugun else "-"

    get_gugun_name.short_description = "구군"

    def get_dong_name(self, obj):
        return obj.dong.dong_name if obj.dong else "-"

    get_dong_name.short_description = "동"

    def get_full_address(self, obj):
        if not obj.dong:
            return "-"
        address = f"{obj.dong.sido.sido_name} {obj.dong.gugun.gugun_name} {obj.dong.dong_name} {obj.main_num}"
        if obj.sub_num:
            address += f"-{obj.sub_num}"
        return address

    get_full_address.short_description = "지번 주소"
