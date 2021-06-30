from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Query, Path

app = FastAPI()

'''
路径参数及校验 Path
'''
# 路径参数总是必需的，因为它必须是路径的一部分。所以，你应该在声明时使用 ... 将其标记为必需参数。


@app.get('/items/{item_id}')
#async def read_items(    item_id: int = Path(..., title="标题"),    q: Optional[str] = Query(None, alias="item-query"),):
# async def read_items(q: str, item_id: int = Path(..., title="标题")):# q没有默认值，应该放在参数前面
# async def read_items(*,item_id:int=Path(...,title="标题"),q:str):# 参数q 没有使用Query,没有默认值放在了item_id后面,因此前面必须使用*,后面的参数都作为kwargs(键值对)来调用
async def read_items(*,item_id:int=Path(...,title="标题",ge=1),q:str):#ge greater than 大于或等于equal,gt 大于,le less than 小于或等于 equal
    results = {"item_id": item_id}
    if q:
        results.update({'q': q})
    return results
