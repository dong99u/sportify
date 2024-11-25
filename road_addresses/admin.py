from django.contrib import admin
from .models import RoadAddress


@admin.register(RoadAddress)
class RoadAddressAdmin(admin.ModelAdmin):
    list_display = [
        "get_full_address",
        "postal_code",
        "get_sido_name",
        "get_gugun_name",
        "get_dong_name",
        "road_name",
        "building_name",
        "get_building_number",
    ]

    list_filter = [
        "dong__sido",
        "dong__gugun",
        "dong",
    ]

    search_fields = [
        "postal_code",
        "road_name",
        "building_name",
        "dong__dong_name",
        "dong__gugun__gugun_name",
        "dong__sido__sido_name",
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

    def get_building_number(self, obj):
        number = str(obj.building_main_num)
        if obj.building_sub_num:
            number += f"-{obj.building_sub_num}"
        return number

    get_building_number.short_description = "건물번호"

    def get_full_address(self, obj):
        if not obj.dong:
            return "-"
        address = f"{obj.dong.sido.sido_name} {obj.dong.gugun.gugun_name} {obj.dong.dong_name} {obj.road_name} {obj.building_main_num}"
        if obj.building_sub_num:
            address += f"-{obj.building_sub_num}"
        if obj.building_name:
            address += f" ({obj.building_name})"
        return address

    get_full_address.short_description = "도로명 주소"
