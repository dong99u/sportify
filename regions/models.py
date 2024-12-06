# regions/models.py
from django.db import models
from common.models import Common
import os


def sido_image_path(instance, filename):
    # 시도 이름을 영문으로 매핑
    name_mapping = {
        "서울특별시": "seoul",
        "부산광역시": "busan",
        "대구광역시": "daegu",
        "인천광역시": "incheon",
        "광주광역시": "gwangju",
        "대전광역시": "daejeon",
        "울산광역시": "ulsan",
        "세종특별자치시": "sejong",
        "경기도": "gyeonggi",
        "강원도": "gangwon",
        "충청북도": "chungbuk",
        "충청남도": "chungnam",
        "전라북도": "jeonbuk",
        "전라남도": "jeonnam",
        "경상북도": "gyeongbuk",
        "경상남도": "gyeongnam",
        "제주특별자치도": "jeju",
    }

    # 원본 파일의 확장자 가져오기
    ext = filename.split(".")[-1]
    # 시도 이름을 영문으로 변환
    eng_name = name_mapping.get(instance.ctprvn_nm, "unknown")
    # 새 파일명 생성 (영문 이름 + 확장자)
    new_filename = f"{eng_name}.{ext}"

    return os.path.join("sido_images", new_filename)


class Sido(Common):
    ctprvn_nm = models.CharField(max_length=20, verbose_name="시/도 이름")
    image = models.ImageField(
        upload_to=sido_image_path, null=True, blank=True, verbose_name="시/도 이미지"
    )

    class Meta:
        db_table = "sido"
        verbose_name = "시/도"
        verbose_name_plural = "시/도 목록"

    def __str__(self):
        return self.ctprvn_nm

    def save(self, *args, **kwargs):
        if self.image:
            # 기존 이미지가 있으면 삭제
            try:
                old_instance = Sido.objects.get(pk=self.pk)
                if old_instance.image != self.image:
                    old_instance.image.delete(save=False)
            except Sido.DoesNotExist:
                pass
        super().save(*args, **kwargs)


class Facility(Common):
    sido = models.ForeignKey(
        Sido, on_delete=models.CASCADE, related_name="facilities", verbose_name="시/도"
    )
    fclty_nm = models.CharField(max_length=100, verbose_name="시설 이름")
    fclty_addr = models.CharField(max_length=100, verbose_name="도로명 주소")

    class Meta:
        db_table = "facility"
        verbose_name = "시설"
        verbose_name_plural = "시설 목록"

    def __str__(self):
        return self.fclty_nm

