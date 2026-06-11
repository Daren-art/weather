Веб-приложение для просмотра текущей погоды по названию города.

Проект написан на FastAPI и использует Open-Meteo API для получения погодных данных.

## Возможности

- Поиск погоды по названию города
- Отображение текущей температуры
- Отображение скорости ветра
- Серверный рендеринг HTML через Jinja2
- Асинхронные запросы через httpx
- Подключение PostgreSQL

## Стек технологий

- FastAPI
- PostgreSQL
- SQLAlchemy
- Jinja2
- httpx
- Uvicorn

## Установка

Клонируйте репозиторий:
```bash

git clone <https://github.com/Daren-art/weather>
cd weather_app

Создайте виртуальное окружение:

python -m venv venv

Активируйте его.

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

Установите зависимости:

pip install -r req.txt

Настройка PostgreSQL

Создайте базу данных:

CREATE DATABASE weather_db;

Создайте файл .env:

DATABASE_URL=postgresql://postgres:password@localhost/weather_db

Замените:

postgres — на имя пользователя PostgreSQL
password — на ваш пароль
weather_db — на название вашей базы данных
Запуск проекта

Запустите сервер:

uvicorn app.main:app --reload

После запуска приложение будет доступно по адресу:

http://127.0.0.1:8000

Используемое API

Для получения данных о погоде используется Open-Meteo.
```
## Алгоритм работы:

Пользователь вводит название города.
Приложение получает координаты города через Geocoding API.
По координатам запрашивается текущая погода.
Результат отображается пользователю.