# 기본 이미지로 Python 3.10 사용
FROM python:3.10-slim

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치
RUN curl -sSL https://install.python-poetry.org | python3 -

# 작업 디렉토리 설정
WORKDIR /app

# Poetry 설정 파일 복사
COPY pyproject.toml poetry.lock ./

# Poetry 가상환경 비활성화 및 의존성 설치
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# 프로젝트 파일 복사
COPY . .

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=config.settings

# 정적 파일 수집
RUN poetry run python manage.py collectstatic --noinput

# 포트 설정
EXPOSE 8000

# Gunicorn으로 서버 실행
CMD ["poetry", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]