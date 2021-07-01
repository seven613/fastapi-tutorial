from datetime import datetime

from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str = None


app = FastAPI()


@app.put('/items/{id}')
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item) #将数据转为JSON格式
    return(json_compatible_item_data)