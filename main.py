from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# 基本示例
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []

# @app.post('/items/', response_model=Item)
# async def create_item(item: Item):
#     return item

# 返回与输入相同的数据

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# @app.post('/user/', response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# 响应模型编码参数

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "bar描述", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": "baz描述", "price": 50.2, "tax": 10.5, "tags": []},
}


# response_model_exclude_unset 响应数据中默认数据将被排除，只返回模型字段中已经设置的值
@app.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def read_items(item_id: str):
    return items[item_id]


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},  # 只返回name、description字段
)
async def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})  # 排除tax字段
async def read_item_public_data(item_id: str):
    return items[item_id]
