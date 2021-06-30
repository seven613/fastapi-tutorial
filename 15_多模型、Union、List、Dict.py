from typing import Union, List,Dict
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# class BaseItem(BaseModel):
#     description: str
#     type: str


# class CarItem(BaseItem):
#     type = 'car'


# class PlaneItem(BaseItem):
#     type = 'plane'
#     size: int


# items = {
#     "item1": {"description": "All my friends drive a low rider", "type": "car"},
#     "item2": {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }


# @app.get('/items/{item_id}', response_model=Union[CarItem, PlaneItem]) #Union 返回的响应数据必须符合CarItem或PlaneItem中任意一种格式
# async def read_items(item_id: str):
#     return items[item_id]

# #响应模型的List
# class Item(BaseModel):
#     name: str
#     description: str


# items = [
#     {"name": "Foo", "description": "There comes my hero"},
#     {"name": "Red", "description": "It's my aeroplane"},
# ]


# @app.get("/items/", response_model=List[Item])  # 也可以使用模型列表
# async def read_items():
#     return items

#响应模型 字典
@app.get("/keyword-weights/", response_model=Dict[str, float])#返回的模型，必须key:str,value:float形式
async def read_keyword_weights():
    return {"foo": 2.3, "bar": 3.4}