from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connections
from django.db.utils import OperationalError
from django.conf import settings


@api_view(["GET"])
def health_check(request):
    try:
        # 데이터베이스 연결 상태 확인
        db_conn = connections["default"]
        db_conn.cursor()
        db_status = "healthy"
    except OperationalError:
        db_status = "unhealthy"

    # 응답 데이터 구성
    health_status = {
        "status": "healthy",
        "database": db_status,
        "version": getattr(settings, "APP_VERSION", "1.0.0"),
    }

    # 데이터베이스가 unhealthy면 전체 상태도 unhealthy로 설정
    if db_status == "unhealthy":
        health_status["status"] = "unhealthy"
        return Response(health_status, status=503)

    return Response(health_status, status=200)
