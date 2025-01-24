from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def welcome_adm() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{userid}")
async def welcome_user(userid: int = Path(ge=1, le=100, description="Enter User ID", example=5)) -> dict:
    return {"message": f'Вы вошли как пользователь №{userid}'}


# @app.get("/user/{username}/{age}")
# async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter UserName")],
#                     age: Annotated[int, Path(ge=18, le=120, description="Enter your age")]) -> dict:
#     return {"Информация о пользователе": f'Имя: {username}. Возраст: {age}'}


@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter User Name")],
                    age: int = Path(ge=18, le=120, description="Enter your age")) -> dict:
    return {"Информация о пользователе": f'Имя: {username}. Возраст: {age}'}
