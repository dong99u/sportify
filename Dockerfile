<<<<<<< HEAD
# 기본 Python 이미지 사용
FROM python:3.11.7-slim

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 시스템 의존성 설치
=======
FROM python:3.11.7-slim

WORKDIR /app

# Install system dependencies
>>>>>>> 762d9ec22f82cb42aacfc6555481aea787211356
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Configure poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev

# Copy project files
COPY . .

# Collect static files
RUN poetry run python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Start gunicorn
CMD ["poetry", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
