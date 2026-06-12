from pydantic import BaseModel

# общия поля задачи
class TodoBase(BaseModel):
    title: str

# что происходит при создании
class TodoCreate(TodoBase):
    pass

# что отдаём наружу
class TodoRead(TodoBase):
    id: int
    completed: bool



