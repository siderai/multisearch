FROM python:3.10.4-slim-bullseye

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./

RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install
