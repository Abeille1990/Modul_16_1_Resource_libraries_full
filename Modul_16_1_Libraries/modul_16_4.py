from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List


users = []


app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def user_db() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user: User):
    new_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user, {"detail": f'User {new_id} has been registered'}


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, user: User):
    for u in users:
        if u.id == user_id:
            u.username = user.username
            u.age = user.age
            return u, {"detail": f'User {user_id} has been updated'}
    raise HTTPException(status_code=404, detail="User is not found")


@app.delete("/users/{user_id}", response_model=dict)
async def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return {f"User{user_id} is deleted"}
    raise HTTPException(status_code=404, detail="User is not found")
