# Online Cinema API

Цей проєкт — **REST API на FastAPI** для керування системою онлайн-кінотеатру. API забезпечує повноцінний набір **CRUD-операцій** для роботи з основними сутностями медіа-сервісу.

Система дозволяє працювати з:

* фільмами
* акторами
* користувачами
* переглядами фільмів
* звʼязками між фільмами та акторами

Документація API доступна через **Swagger UI**, який автоматично генерується фреймворком FastAPI.

---

## Структура проєкту

```
course_work/
│
├── full coursework.py        # містить логіку роботи REST API
├── online_cinema.sql         #база даних
├── README.md                 # опис курсового проєкту

```

---

## Встановлення та запуск

### 1. Створення віртуального середовища

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 2. Встановлення бібліотек

```bash
pip install fastapi
pip install uvicorn
pip install pymysql
```

### 3. Запуск сервера

```bash
python main.py
```

Сервер запускається за адресою:

```
http://127.0.0.1:8002/
```

Після відкриття адреси у браузері автоматично доступна документація API:

```
http://127.0.0.1:8002/docs
```

Окремо відкривати документацію не потрібно.

---

## Доступні операції

### Actors (Актори)

* `GET /actors` — отримати список акторів
* `POST /actors` — додати актора
* `PUT /actors/{actor_id}` — змінити дані актора
* `DELETE /actors/{actor_id}` — видалити актора

### Movies (Фільми)

* `GET /movies` — отримати список фільмів
* `POST /movies` — додати фільм
* `PUT /movies/{movie_id}` — змінити фільм
* `DELETE /movies/{movie_id}` — видалити фільм

### Users (Користувачі)

* `GET /users` — отримати список користувачів
* `POST /users` — створити користувача
* `PUT /users/{user_id}` — змінити користувача
* `DELETE /users/{user_id}` — видалити користувача

### Views (Перегляди)

* `GET /views` — отримати всі перегляди
* `POST /views` — додати перегляд
* `PUT /views/{view_id}` — змінити перегляд
* `DELETE /views/{view_id}` — видалити перегляд

### Movie_Actors (Фільм – Актор)

* `GET /movie_actors` — отримати всі звʼязки
* `POST /movie_actors` — створити звʼязок
* `PUT /movie_actors/{movie_id}/{actor_id}` — змінити звʼязок
* `DELETE /movie_actors/{movie_id}/{actor_id}` — видалити звʼязок

---

## Автор курсової роботи

Студентка групи ФЕП-23с – Бойчук К.І.

---

## Науковий керівник

Доцент – **Мисюк Р. В.**


