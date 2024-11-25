# Generated by Django 5.1.3 on 2024-11-25 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dong", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoadAddress",
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
                ("road_name", models.CharField(max_length=20, verbose_name="로드명")),
                (
                    "building_main_num",
                    models.PositiveIntegerField(verbose_name="메인_building_num"),
                ),
                (
                    "building_sub_num",
                    models.PositiveIntegerField(verbose_name="부building_num"),
                ),
                (
                    "building_name",
                    models.CharField(max_length=20, verbose_name="building_name"),
                ),
                (
                    "postal_code",
                    models.CharField(max_length=5, verbose_name="우편번호코드"),
                ),
                (
                    "dong",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dong.dong",
                        verbose_name="동",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
