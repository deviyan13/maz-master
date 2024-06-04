# Используйте официальный образ Python из Docker Hub
FROM python:3.9

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте зависимости в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install -r requirements.txt

# Скопируйте проект в контейнер
COPY . .

# Добавьте команду для выполнения скрипта и запуска сервера
CMD ["sh", "-c", "python manage.py migrate && python import_data.py && python manage.py runserver 0.0.0.0:8000"]
