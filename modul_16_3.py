# Задача "Имитация работы с БД":
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
# Реализуйте 4 CRUD запроса:
# get запрос по маршруту '/users', который возвращает словарь users.
# post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь
# по максимальному по значению ключом значение строки "Имя: {username},
# возраст: {age}". И возвращает строку "User <user_id> is registered".
# put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет
# значение из словаря users под ключом user_id на строку "Имя: {username},
# возраст: {age}". И возвращает строку "The user <user_id> is updated"
# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users
# по ключу user_id пару.
# Выполните каждый из этих запросов по порядку. Ответы должны совпадать:
# 1. GET '/users'
# {
# "1": "Имя: Example, возраст: 18"
# }
# 2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
# "User 2 is registered"
# 3. POST '/user/{username}/{age}' # username - NewUser, age - 22
# "User 3 is registered"
# 4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
# "User 1 has been updated"
# 5. DELETE '/user/{user_id}' # user_id - 2
# "User 2 has been deleted"
# 6. GET '/users'
# {
# "1": "Имя: UrbanProfi, возраст: 28",
# "3": "Имя: NewUser, возраст: 22"
# }
# Пример результата выполнения программы:
# Как должен выглядеть Swagger:
#
#
# Примечания:
# Не забудьте написать валидацию для каждого запроса, аналогично предыдущему заданию.
from fastapi import FastAPI
from typing import Annotated
from fastapi import Path

app = FastAPI()

users = [{"user_id": 1, "username": 'Example', "age": '18'}]


@app.get("/users")
async def get_user() -> list:
    return users


@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(min_length=5,
                                  max_length=20, regexp="^[a-zA-Z0-9_-]+$",
                                  description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
) -> str:
    # new_id = int(len(users) + 1)
    new_id = len(users) + 1
    new_user = {"user_id": new_id, "username": username, 'age': age}
    users.append(new_user)
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_massage(
    user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")],
    username: Annotated[str, Path(min_length=5,
                                  max_length=20, regexp="^[a-zA-Z0-9_-]+$",
                                  description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
) -> str:
    for user in users:
        if user["user_id"] == user_id:
            user["username"] = username
            user["age"] = age
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID")]
) -> str:
    for i, user in enumerate(users):
        if user["user_id"] == user_id:
            del users[i]
    return f"User {user_id} has been deleted"
