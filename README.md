# FastAPI Task Tracker

Учебный REST API проект для управления задачами на FastAPI и SQLAlchemy. Демонстрирует чистую архитектуру, асинхронное программирование и работу с базой данных.

## О проекте

Это простое приложение для создания и просмотра задач (TODO-листа) с использованием современного стека технологий Python.

## Стек технологий

- **FastAPI 0.115.8** - веб-фреймворк для создания API
- **SQLAlchemy 2.0.38** - ORM для работы с базой данных
- **SQLite + aiosqlite** - легковесная асинхронная база данных
- **Pydantic 2.10.6** - валидация данных
- **Uvicorn 0.34.0** - ASGI сервер
- **Python 3.13**

## Архитектура

Проект использует многослойную архитектуру:

```
HTTP запрос
    ↓
router.py (API endpoints)
    ↓
repository.py (бизнес-логика)
    ↓
database.py (ORM модели)
    ↓
tasks.db (SQLite)
```

## Установка и запуск

### Требования

- Python 3.13+
- pip

### Локальный запуск

1. **Клонировать репозиторий**
```bash
git clone https://github.com/yourusername/fastapi-tracker-tasks.git
cd fastapi-tracker-tasks
```

2. **Создать виртуальное окружение**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Установить зависимости**
```bash
pip install -r requirements.txt
```

4. **Запустить приложение**
```bash
uvicorn main:app --reload
```

API доступен по адресу: `http://localhost:8000`

## Использование

### Интерактивная документация

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### API Endpoints

**POST /tasks** - Создать задачу

Запрос:
```json
{
  "name": "Название задачи",
  "description": "Описание (опционально)"
}
```

Ответ:
```json
{
  "ok": true,
  "task_id": 1
}
```

**GET /tasks** - Получить все задачи

Ответ:
```json
[
  {
    "id": 1,
    "name": "Название задачи",
    "description": "Описание"
  }
]
```

## Структура проекта

```
fastapi-tracker-tasks/
├── main.py           # Точка входа приложения
├── database.py       # Конфигурация БД и ORM модели
├── schemas.py        # Pydantic схемы для валидации
├── router.py         # API endpoints
├── repository.py     # Работа с базой данных
├── requirements.txt  # Зависимости
├── Dockerfile        # Docker конфигурация
└── README.md         # Этот файл
```

### Описание файлов

- **main.py** - инициализация FastAPI, подключение роутеров
- **database.py** - настройка SQLAlchemy, модель `TaskOrm` (id, name, description)
- **schemas.py** - схемы Pydantic для валидации (`STaskAdd`, `STask`, `STaskId`)
- **router.py** - обработчики для POST и GET запросов
- **repository.py** - паттерн Repository для работы с БД

## Как это работает

### Поток данных при создании задачи:

1. Клиент отправляет POST запрос на `/tasks`
2. `router.py` принимает и валидирует данные через Pydantic
3. `repository.py` создает объект ORM и сохраняет в БД
4. `database.py` выполняет асинхронный INSERT в SQLite
5. Клиент получает `task_id` созданной задачи

### Схема базы данных

Таблица `tasks`:
- `id` (INTEGER, PRIMARY KEY)
- `name` (TEXT, NOT NULL)
- `description` (TEXT, NULL)

## Docker

```bash
# Собрать образ
docker build -t fastapi-tracker-tasks .

# Запустить контейнер
docker run -p 8000:80 fastapi-tracker-tasks
```

## Автор

Даниил Урасинов

## Лицензия

Проект сделан в рамках учебного проекта
