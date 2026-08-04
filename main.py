from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from pydantic import BaseModel
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import Task
from database import Base, engine
import models

app = FastAPI()

tasks: list[Task] = []
Base.metadata.create_all(bind=engine)

# html templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
# получить страничку index.html
@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {})

# выложить задачу
@app.post('/tasks')
def create_task(task: Task):
    tasks.append(task)
    return task

# получить все задачи
@app.get('/tasks')
def get_tasks():
    return tasks

# переключить состояние задачи
@app.put('/tasks/{task_id}')
def toggle_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.done = not task.done
            return task
    raise HTTPException(status_code=404, detail='Task not found')

# удалить задачу
@app.delete('/tasks/{task_id}')
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {'message': 'Task deleted'}
    raise HTTPException(status_code=404, detail='Task not found')










if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)