# Наследуем образ Python
FROM python:3.10-slim-buster

# Копируем файлы проекта
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# Устанавливаем poetry
RUN pip3 install --upgrade pip && pip3 install poetry

# Устанавливаем зависимости с помощью poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Копируем остальные файлы проекта
COPY . /app

EXPOSE 8000


# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]