from fastapi import APIRouter
from schemas.todo import TodoCreate

router = APIRouter(prefix='/todos', tags=['todos_roots'])

@router.get('/')
async def get_todos():
    return []

@router.post('/')
async def create_todo(todo: TodoCreate):
    return todo


