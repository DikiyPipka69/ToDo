from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

# основная ручка
@app.get('/')
def read_root():
    return {"message": "Hello, World!"}



















if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)