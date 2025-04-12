#!/bin/bash

# Останавливаем и удаляем старые контейнеры, если они существуют
echo "Stopping and removing old containers..."
docker-compose down

# Сборка Docker образа
echo "Building Docker image..."
docker-compose build

# Выполнение миграций
echo "Running migrations..."
docker-compose run --rm django python teplica/manage.py makemigrations
docker-compose run --rm django python teplica/manage.py migrate

# Сборка статики
echo "Collecting static files..."
docker-compose run --rm django python teplica/manage.py collectstatic --noinput

# Запуск контейнера
echo "Starting the container..."
docker-compose up
