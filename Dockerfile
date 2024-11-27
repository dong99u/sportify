FROM python:3.10.12-slim

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Poetry 설치 및 PATH 설정
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# 작업 디렉토리 설정
WORKDIR /app

# Poetry 설정 파일 복사
COPY pyproject.toml poetry.lock ./

# 의존성 설치
RUN poetry install --no-interaction --no-ansi

# 프로젝트 파일 복사
COPY . .

# gunicorn으로 서버 실행
CMD ["poetry", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]