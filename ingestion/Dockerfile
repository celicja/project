FROM python:3.12-slim

WORKDIR /app

RUN pip install poetry

ENV PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

COPY . .

CMD ["sleep", "infinity"]