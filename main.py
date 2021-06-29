from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Query, Path

app = FastAPI()

'''
路径参数及校验 Path
'''

#路径参数总是必需的，因为它必须是路径的一部分。所以，你应该在声明时使用 ... 将其标记为必需参数。
@app.get('/items/{item_id}')
async def read_items(
    item_id: int = Path(..., title="标题"),
    q: Optional[str] = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
