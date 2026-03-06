FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virutalenvs.create false \
    && poetry install --no-interaction \

COPY . .

CMD["sleep", "infinity"]