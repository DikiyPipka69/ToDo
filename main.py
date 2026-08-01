from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from pydantic import BaseModel
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Task

app = FastAPI()

tasks: list[Task] = []

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# получить страничку index.html
@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

@app.post('/tasks')
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get('/tasks')
def get_tasks():
    return tasks
















if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)