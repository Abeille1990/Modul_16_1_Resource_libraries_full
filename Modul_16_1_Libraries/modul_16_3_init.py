from fastapi import FastAPI, Path
from typing import Annotated
from fastapi import HTTPException

users = [{'id': 1, 'Имя': 'Example', 'Возраст': 18}]


app = FastAPI()


@app.get("/users")
async def user_db():
    return users


@app.post("/users")
async def create_user(name: str, age: int):
    new_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {"id": new_id, "Имя": name, "Возраст": age}
    users.append(new_user)
    return new_user, {"detail": f'User {new_id} has been registered'}


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, name: str, age: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            user["Имя"] = name
            user["Возраст"] = age
            return user, {"detail": f'User {user_id} has been updated'}
    raise HTTPException(status_code=404, detail="User is not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {f"User{user_id} is deleted"}
    raise HTTPException(status_code=404, detail="User is not found")
