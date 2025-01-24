from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def welcome_adm() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{userid}")
async def welcome_user(userid: int) -> str:
    return f'Вы вошли как пользователь №{userid}'


@app.get("/user")
async def user_info(user_name: str, user_age: float) -> str:
    return f' Информация о пользователе": Имя: {user_name}. Возраст: {user_age}'
