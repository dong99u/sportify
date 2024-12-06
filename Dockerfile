# 기본 Python 이미지 사용
FROM python:3.11.7-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 시스템 의존성 설치
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치
RUN pip install poetry

# Poetry 가상환경 생성하지 않도록 설정
RUN poetry config virtualenvs.create false

# 프로젝트 의존성 파일 복사
COPY pyproject.toml poetry.lock ./

# 프로젝트 의존성 설치
RUN poetry install --no-dev --no-root

# 프로젝트 파일 복사
COPY . .

# media와 static 디렉토리 생성
RUN mkdir -p media/sido_images staticfiles

# static 파일 수집
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV SECRET_KEY="yth9(nv(&xq8wr*qll#k&fxjk1_-n$m#!xilu%q3mwpeixfy_*"
ENV DEBUG=False
RUN poetry run python manage.py collectstatic --noinput

# gunicorn 설정
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]
