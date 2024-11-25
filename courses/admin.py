from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "sports_center",
        "price",
        "start_date",
        "end_date",
        "status",
    ]

    list_filter = [
        "category",
        "sports_center",
        "status",
        "start_date",
        "end_date",
    ]

    search_fields = [
        "title",
        "description",
        "category__name",
        "sports_center__center_name",
    ]

    readonly_fields = ["created_at", "updated_at"]

    fieldsets = [
        (
            "기본 정보",
            {
                "fields": (
                    "title",
                    "description",
                    "category",
                    "sports_center",
                    "price",
                    "image",
                    "course_link",
                )
            },
        ),
        (
            "수강 일정",
            {
                "fields": (
                    "start_date",
                    "end_date",
                    "start_time",
                    "end_time",
                )
            },
        ),
        (
            "수강 현황",
            {
                "fields": (
                    "status",
                    "current_enrollment",
                    "capacity",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    ]
