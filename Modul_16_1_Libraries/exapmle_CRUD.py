from fastapi import FastAPI
from fastapi import HTTPException

tasks = [{"id": 1, "description": "Изучить CRUD в FastAPI"},
         {"id": 2, "description": "Написать примеры кода"}]

apptest = FastAPI()


@apptest.get("/tasks")
async def get_tasks():
    return tasks


@apptest.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

# Описание кода:
# # # @app.get("/tasks/{task_id}"): Декоратор маршрута, привязывает GET-запрос /tasks/{task_id} к функции get_task.
# # # task_id: int: FastAPI автоматически преобразует task_id в int.
# # # Если передать нецелое число, будет возвращена ошибка.


# Create (POST): Создание новой задачи

@apptest.post("/tasks")
async def create_task(description: str):
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    new_task = {"id": new_id, "description": description}
    tasks.append(new_task)
    return new_task

#
# Описание кода:
# description: str: Входной параметр функции, будет передан в теле запроса. Например Новая задача
# new_id: Уникальный ID для новой задачи. Если список задач пуст, начнем с 1.
# Неочевидный момент: FastAPI автоматически проверяет, что description является строкой.

# Метод PUT заменяет существующую запись новой. В нашем примере это будет обновление описания задачи по её ID.
# Пример: Обновить задачу по ID


@apptest.put("/tasks/{task_id}")
async def update_task(task_id: int, description: str):
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
        return task
    raise HTTPException(status_code=404, detail="Задача не найдена")

# Описание кода:
# task_id: int: Параметр маршрута, уникальный идентификатор задачи.
# Можно по id изменить описание задачи. Вводим id = 3 , меняем description на: Не останавливаться на достигнутом

# Неочевидный момент: FastAPI не проверяет, что задача с таким ID существует, если не добавить это вручную,
# как мы сделали через HTTPException.


@apptest.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
    return {"detail": "Задача удалена"}
    raise HTTPException(status_code=404, detail="Задача не найдена")
