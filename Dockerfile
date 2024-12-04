FROM python:3.11-slim

# 기본 패키지 설치
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential pkg-config curl && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉터리 설정
WORKDIR /app

# Poetry 설치
RUN pip install poetry
RUN poetry config virtualenvs.create false

# 의존성 복사 및 설치
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

# 프로젝트 파일 복사
COPY . .

# 정적 파일 수집
RUN python manage.py collectstatic --noinput

# 권장: 비루트 사용자 설정
RUN adduser --disabled-password appuser
USER appuser

# Gunicorn 실행
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]
