from django.contrib import admin
from .models import Sido


@admin.register(Sido)
class SidoAdmin(admin.ModelAdmin):
    list_display = [
        "sido_name",
        "created_at",
        "updated_at",
    ]

    search_fields = [
        "sido_name",
    ]

    readonly_fields = ["created_at", "updated_at"]
