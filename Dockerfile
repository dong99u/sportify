FROM python:3.10.12-slim

WORKDIR /app

# 시스템 패키지 설치
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치
RUN pip install poetry

# Poetry 가상 환경 생성하지 않도록 설정
RUN poetry config virtualenvs.create false

# 프로젝트 의존성 파일 복사
COPY pyproject.toml poetry.lock ./

# 의존성 설치
RUN poetry install --no-dev --no-root

# 프로젝트 파일 복사
COPY . .

# 서버 실행
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]