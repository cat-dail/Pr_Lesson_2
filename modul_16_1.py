from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/users/{user_id}")
async def get_user_id(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}


@app.get("/users")
async def get_username(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
