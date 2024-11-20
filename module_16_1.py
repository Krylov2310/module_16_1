from fastapi.responses import HTMLResponse
from fastapi import FastAPI

app = FastAPI()

# запуск - python -m uvicorn module_16_1:app
info_ed = ('Домашнее задание по теме "Основы Fast Api и маршрутизация".<br>'
           'Цель: научиться создавать базовую маршрутизацию для обработки данных в FastAPI.<br>'
           'Задача "Начало пути":<br>'
           'Студент Крылов Эдуард Васильевич<br>'
           'Дата: 20.11.2024г.')


# http://127.0.0.1:8000/
@app.get("/")
async def welcome() -> str:
    return "Главная страница"


# http://127.0.0.1:8000/user/admin
@app.get("/user/admin")
async def id_admin() -> str:
    return "Вы вошли как администратор"


# http://127.0.0.1:8000/user/123
@app.get("/user/{user_id}")
async def id_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


# http://127.0.0.1:8000/user?username=Ed&age=46
@app.get("/user")
async def users(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: '{username}', Возраст: '{age}'"


# http://127.0.0.1:8000/info
@app.get("/info", response_class=HTMLResponse)
async def info() -> str:
    return info_ed
