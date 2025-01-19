from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from app.routers import task, user

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)