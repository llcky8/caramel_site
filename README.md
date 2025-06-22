# Social Media Marketing — Django SPA

Это одностраничное приложение (SPA) для управления кейсами агентства Social Media Marketing.

## Описание

Проект реализован на Django. Через административную панель можно добавлять, редактировать и удалять кейсы с изображениями и описанием.

## Структура проекта
```
caramel_site/
├── db.sqlite3                 # база данных SQLite 
├── manage.py                  # главный скрипт для управления проектом Django
├── requirements.txt           # файл со списком зависимостей Python
├── caramel_site
|   ├── asgi.py                # интерфейсы для запуска проекта на сервере
|   ├── settings.py            # конфигурация проекта
|   ├── urls.py                # интерфейсы для запуска проекта на сервере
|   ├── wsgi.py                # маршрутизация URL-адресов проекта
├── cases
|   ├── admin.py               # регистрация моделей в административной панели Django
|   ├── apps.py                # настройки приложения
|   ├── models.py              # модели базы данных
|   ├── tests.py               # тесты для приложения
|   ├── views.py               # логика обработки запросов и возврата ответов
|   ├── migrations             # миграции базы данных (файлы для создания/обновления таблиц)
|   ├── static
|   |   ├── cases              # css-файлы стилей
|   |   ├── img                # изображения для сайта
|   ├── templates
|   |   ├── cases              # HTML-шаблоны для отображения страниц        
```
## Требования

- Python 3.11 или выше
- pip (рекомендуется последняя версия)
Для обновления pip до последней версии:
```bash
python -m pip install --upgrade pip
```

### 1. Установить

Установите Python [с официального сайта](https://www.python.org/downloads/), версия 3.11 или новее.

### 2. Клонировать репозиторий:

```bash
git clone https://github.com/llcky8/caramel_site
cd caramel_site
```

### 3. Создать виртуальное окружение:
```bash
python -m venv venv
```

### 4. Активируйте виртуальное окружение:
На Windows:
```bash
.\venv\Scripts\activate
```
На Linux/Mac:
```bash
source venv/bin/activate
```

### 5. Установить зависимости:

```bash
pip install -r requirements.txt
```
### 6. Выполнить миграции базы данных:

```bash
python manage.py migrate
```

### 7. Создать суперпользователя (администратора):

```bash
python manage.py createsuperuser
```

### 8. Запустить сервер разработки:

```bash
python manage.py runserver
```

### 9. Открыть в браузере:

```cpp
http://127.0.0.1:8000/
```
Админка доступна по адресу:
```
http://127.0.0.1:8000/admin/
```
> cольный проект автора на инициативе и пары суток без кс
