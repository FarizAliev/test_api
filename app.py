from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"User": "Fariz","age": 28}


@app.get("/items/{id}")
def read_item(id: int, q: Union[str, None] = None):
    return {"item_id": id*2, "q": q}