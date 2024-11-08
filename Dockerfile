FROM ubuntu:latest
LABEL authors="bezrezentlnh"

ENTRYPOINT ["top", "-b"]

# Указываем базовый образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Добавляем файл credentials.json в контейнер
COPY google_parser/credentials.json /app/google_parser/credentials.json

# Указываем команду для запуска приложения
CMD ["python", "google_parser/main.py"]