FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv@sha256:2381d6aa60c326b71fd40023f921a0a3b8f91b14d5db6b90402e65a635053709 /uv /uvx /bin/

WORKDIR /app/web
COPY . /app/web

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
        python3-dev \
    && uv sync --dev \
    && rm -rf /var/lib/apt/lists/*
