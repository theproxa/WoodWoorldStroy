# Используем официальный образ Python
FROM python:3.9



# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . .


# Команда для запуска сервера разработки
CMD ["python", "./WoodWoorldStroy/manage.py", "runserver", "0.0.0.0:8000"]
