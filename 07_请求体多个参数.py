from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Query, Path, Body

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None

# 混合使用Path、Query和请求体参数
# @app.put('/items/{item_id}')
# async def update_item(
#     *,
#     item_id: int = Path(..., title="标题", ge=0, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({'q': q})
#     if item:
#         results.update({'q': q})
#     return results


# 多个请求体
# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     }
# }


# 请求体中的单一值
# @app.put('/items/{item_id}')
# async def update_item(item_id: int, item: Item, user: User, importance: int = Body(...)):# 单一值使用Body参数
#     results = {"item_id": item_id, "item": item,
#                "user": user, importance: importance}
#     return results

# #参数格式：
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     },
#     "user": {
#         "username": "dave",
#         "full_name": "Dave Grohl"
#     },
#     "importance": 5
# }


# 多个请球体参数和查询参数

# @app.put('/items/{item_id}')
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(..., gt=0),
#     q: Optional[str] = None
# ):
#     results = {"item_id": item_id, "item": item,
#                "user": user, "importance": importance}
#     if q:
#         results.update({'q': q})
#     return results

# 嵌入单个请求体参数， Body(..., embed=True) 将
@app.put("/items/{item_id}")
async def update_item(
    item_id: int, 
    #user:User, #什么都不加，必须放在Body前面，否则报错
    item: Item = Body(..., embed=False)):
    results = {'item_id': item_id, "item": item}
    return results
