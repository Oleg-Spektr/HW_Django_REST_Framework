# LMS-платформа на Django REST Framework

Бэкенд-часть SPA-приложения для онлайн-обучения.

## Реализованный функционал
* Кастомная модель пользователя `User` (авторизация по `email`, поля: телефон, город, аватар).
* Приложение `materials` с моделями `Course` и `Lesson` (связь `ForeignKey`).
* CRUD для курсов реализован на базе `ModelViewSet`.
* CRUD для уроков реализован на базе `Generic`-классов.
* Эндпоинт для просмотра и редактирования профиля пользователя (`RetrieveUpdateAPIView`).

## Запуск проекта
1. Клонируйте репозиторий и создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # для Windows: venv\Scripts\activate
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Примените миграции и запустите сервер:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
