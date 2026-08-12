from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn
import models
import schemas
from database import Base, engine, get_db
from models import Task as TaskModel

# инициализация приложения
app = FastAPI()
# созданице табоиц в базе данных
Base.metadata.create_all(bind=engine)
# подключение templates и static
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# получить html страницу
@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {})


# получить все задачи из базы данных
@app.get('/tasks', response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()

# создать задачу в базе данных
@app.post('/tasks', response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# переключить состояние задачи в базе данных (завершено/не завершено)
@app.put('/tasks/{task_id}', response_model=schemas.TaskResponse)
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail='Task not found')
    db_task.done = not db_task.done
    db.commit()
    db.refresh(db_task)
    return db_task

# удалить задачу из базы данных
@app.delete('/tasks/{task_id}')
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail='Task not found')
    db.delete(db_task)
    db.commit()
    return {'message': 'Task deleted'}



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)