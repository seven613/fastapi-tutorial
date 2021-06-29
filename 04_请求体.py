from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI

# 声明数据模型


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()

'''
请求体中的路径参数、查询参数
'''


@app.post('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    # **item.dict()解包，将字典中的k,v 全部输出
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result
