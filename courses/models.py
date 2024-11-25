# courses/models.py
from django.db import models
from django.core.validators import MinValueValidator
from common.models import Common


class Course(Common):
    class StatusChoices(models.TextChoices):
        RECRUITING = "RECRUITING", "모집중"
        CLOSED = "CLOSED", "마감"
        COMPLETED = "COMPLETED", "종료"

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="카테고리",
    )

    sports_center = models.ForeignKey(
        "centers.SportsCenter",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="SPORTS CENTER",
    )

    # 기본 정보
    title = models.CharField(max_length=255, verbose_name="강좌 제목")
    description = models.TextField(verbose_name="강좌 설명")
    price = models.IntegerField(
        validators=[MinValueValidator(0)], verbose_name="수강료"
    )

    image = models.ImageField(
        upload_to="courses/images/%Y/%m/%d/",
        verbose_name="강좌 이미지",
        null=True,
        blank=True,
    )

    course_link = models.URLField(
        max_length=200,
        verbose_name="강좌 홈페이지 링크",
        help_text="강좌 상세 정보를 볼 수 있는 링크를 입력하세요",
    )

    # 수강 일정
    start_time = models.TimeField(verbose_name="강의 시작 시간")
    end_time = models.TimeField(verbose_name="강의 종료 시간")
    start_date = models.DateField(verbose_name="강의 시작일")
    end_date = models.DateField(verbose_name="강의 종료일")

    # 수강 현황
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.RECRUITING,
        verbose_name="운영상태",
    )
    current_enrollment = models.PositiveIntegerField(
        default=0, verbose_name="현재 등록 인원"
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], verbose_name="정원"
    )

    class Meta:
        verbose_name = "강좌"
        verbose_name_plural = "강좌 목록"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def is_available(self):
        """수강 신청이 가능한지 확인"""
        return (
            self.status == self.StatusChoices.RECRUITING
            and self.current_enrollment < self.capacity
        )

    def get_remaining_seats(self):
        """남은 자리 수 반환"""
        return self.capacity - self.current_enrollment

    def get_enrollment_rate(self):
        """수강 신청률 반환 (%)"""
        return (self.current_enrollment / self.capacity) * 100
