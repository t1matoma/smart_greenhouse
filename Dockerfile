FROM python:3.10-slim

WORKDIR /app

COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт для Django
EXPOSE 8000

CMD ["python", "teplica/manage.py", "runserver", "0.0.0.0:8000"]
