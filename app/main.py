from fastapi import FastAPI
import uvicorn
from routers.todos import router as todos_router


app = FastAPI()
app.include_router(todos_router)


@app.get("/", tags=['HelloWorld_root'])
async def root():
    return {"message": "Hello World"}




if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)




