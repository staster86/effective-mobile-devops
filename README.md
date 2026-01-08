# Тестовое задание DevOps — Effective Mobile
Простое веб-приложение, развёрнутое в Docker-контейнерах: Python-backend за reverse-прокси nginx, оркестрация через Docker Compose.

## Используемые технологии
- **Docker** — контейнеризация
- **Docker Compose** — оркестрация сервисов
- **Python 3.12** — backend (минимальный HTTP-сервер на базе `http.server`)
- **nginx 1.25** — reverse proxy
- **Git** — контроль версий

## Архитектура и схема взаимодействия
Проект состоит из двух сервисов, связанных через внутреннюю Docker-сеть:
Пользователь (хост)
│
▼
curl http://localhost:80
│
▼
nginx (порт 80 опубликован наружу)
│
▼ (proxy_pass → backend:8080)
backend (порт 8080 — только внутри сети em-network)
│
▼
"Hello from Effective Mobile!"


- **Backend** — минимальный HTTP-сервер на Python, слушает только порт 8080 внутри контейнера. Доступен исключительно из Docker-сети, с хоста напрямую недоступен.
- **Nginx** — reverse proxy, принимает запросы с хоста на порт 80 и перенаправляет их на backend по имени сервиса. Передаёт стандартные заголовки (`Host`, `X-Real-IP`, `X-Forwarded-For`, `X-Forwarded-Proto`).

## Структура проекта
.
├── backend/
│   ├── Dockerfile
│   └── app.py
├── nginx/
│   └── nginx.conf
├── docker-compose.yml
├── README.md
└── .gitignore


## Как запустить проект
1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/staster86/effective-mobile-devops.git
   cd effective-mobile-devops

2. Соберите и запустите контейнеры:
    ```bash
    docker-compose up --build -d

## Отладка
1. Проверьте статус контейнеров:
    ```bash
    docker ps (Должны быть видны два контейнера: em-nginx и em-backend.)

2. Проверить работоспособность:
    ```bash
    curl http://localhost (Ожидаемый ответ "Hello from Effective Mobile!")

## Как остановить и удалить контейнеры
    ```bash
    docker-compose down