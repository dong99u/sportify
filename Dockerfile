FROM python:3.11-slim

WORKDIR /app

# 기본 시스템 패키지 설치
RUN apt-get update \
    && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치 및 설정
RUN pip install poetry
RUN poetry config virtualenvs.create false

# 프로젝트 의존성 설치
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev

# 애플리케이션 코드 복사
COPY . .

# 정적 파일 수집
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "config.wsgi:application"]