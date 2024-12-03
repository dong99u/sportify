from rest_framework import serializers
from .models import Sido


class SidoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Sido
        fields = ["id", "ctprvn_nm", "image", "image_url", "created_at", "updated_at"]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get("request")
            if request:
                return request.build_absolute_uri(obj.image.url)
        return None
