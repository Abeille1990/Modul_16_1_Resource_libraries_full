from fastapi import FastAPI, Query
from typing import Annotated
import uvicorn

app = FastAPI()


users = {
        '1': 'Имя: Examples, возраст: 18'
}

@app.get('/users')
async def return_dict():
    return users


@app.post('/users/{username}/{age}')
async def put_user(username: Annotated[str| None, Query(max_length=50, min_length=1)],
                   age: Annotated[int| None, Query(ge=10, le=150)]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f'User {user_id} is registered'


@app.put('/users/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int| None, Query(ge=1, le=len(users))],
                      username: Annotated[str | None, Query(max_length=50, min_length=1)],
                      age: Annotated[int | None, Query(ge=10, le=150)]):
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.delete('/users/{user_id}')
async def delete_user(user_id: Annotated[int| None, Query(ge=1, le=len(users))]):
    del users[str(user_id)]
    return f"User {user_id} has been deleted"


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
