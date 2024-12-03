from rest_framework import serializers
from .models import Program


class ProgramSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.fclty_ty_nm", read_only=True)
    facility_name = serializers.CharField(source="facility.fclty_nm", read_only=True)
    region = serializers.CharField(source="facility.sido.ctprvn_nm", read_only=True)
    days_display = serializers.CharField(
        source="get_days_display_korean", read_only=True
    )
    time_range = serializers.CharField(source="get_time_range", read_only=True)
    region_image = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = [
            "id",
            "progrm_nm",
            "category_name",
            "facility_name",
            "region",
            "region_image",
            "progrm_days",
            "days_display",
            "start_time",
            "end_time",
            "time_range",
            "progrm_begin_de",
            "progrm_end_de",
            "progrm_prc",
            "progrm_rcrit_nmpr_co",
            "progrm_trget_nm",
            "hmpg_url",
        ]

    def get_region_image(self, obj):
        request = self.context.get("request")
        if obj.facility.sido.image:
            return (
                request.build_absolute_uri(obj.facility.sido.image.url)
                if request
                else obj.facility.sido.image.url
            )
        return None
