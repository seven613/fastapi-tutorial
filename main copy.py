

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")  # 抛出异常
    return{"item": items[item_id]}


@app.get("/items-header/{item_id}")
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404,
                            detail="Item not found",
                            headers={"X-Error": "There goes my error"}) #自定义头信息
    return items[item_id]
