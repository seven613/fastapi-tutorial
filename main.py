from typing import Optional #引入可选类型，Optional[X] 相当于 Union[X, None]

from fastapi import FastAPI

app = FastAPI()

# 定义临时数据
fake_items_db = [
    {"item_name": 'Foo'},
    {"item_name": 'Bar'},
    {"item_name": 'Baz'},
]

# # 请求路径：http://127.0.0.1:8000/items/?skip=2&limit=2
# @app.get('/items/')
# # 定义参数skip int类型,默认值0,limit:int类型，默认值10
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip:skip+limit]  # 数据切片


@app.get('/items/{item_id}')
async def read_item(item_id: str, q: Optional[str] = None): # item_id 是路径参数，q 是查询参数
    if q:
        return {'item_id': item_id, "q": q}
    return {"item_id": item_id}
