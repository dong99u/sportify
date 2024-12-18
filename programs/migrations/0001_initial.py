# Generated by Django 5.1.3 on 2024-12-01 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
        ("regions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Program",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "progrm_nm",
                    models.CharField(max_length=100, verbose_name="프로그램명"),
                ),
                (
                    "hmpg_url",
                    models.CharField(max_length=100, verbose_name="홈페이지 URL"),
                ),
                (
                    "progrm_estbl_wkday_nm",
                    models.CharField(max_length=10, verbose_name="운영 요일"),
                ),
                (
                    "progrm_estbl_tizn_value",
                    models.CharField(max_length=30, verbose_name="운영 시간"),
                ),
                ("progrm_begin_de", models.DateField(verbose_name="시작일")),
                ("progrm_end_de", models.DateField(verbose_name="종료일")),
                ("progrm_prc", models.IntegerField(verbose_name="수강료")),
                ("progrm_rcrit_nmpr_co", models.IntegerField(verbose_name="모집인원")),
                (
                    "progrm_trget_nm",
                    models.CharField(max_length=30, verbose_name="대상"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="programs",
                        to="categories.category",
                        verbose_name="카테고리",
                    ),
                ),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="programs",
                        to="regions.facility",
                        verbose_name="시설",
                    ),
                ),
            ],
            options={
                "verbose_name": "프로그램",
                "verbose_name_plural": "프로그램 목록",
                "db_table": "program",
            },
        ),
    ]
