from typing import Optional  # 引入可选类型，Optional[X] 相当于 Union[X, None]

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


# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: Optional[str] = None): # item_id 是路径参数，q 是查询参数
#     if q:
#         return {'item_id': item_id, "q": q}
#     return {"item_id": item_id}


# '''请求路径:http://127.0.0.1:8000/items/foo?short=1
# 其中：short =1,short = True ,short=true,short=on,short =yes 都可以，均被转换为bool类型
# '''
# @app.get('/items/{item_id}')
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {'item_id': item_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update({'description': '描述信息'})
#     return item


# '''
# 多路径中的查询参数应用，必须在路径操作函数中定义相同名称即可识别
# '''
# @app.get('/users/{user_id}/items/{item_id}')
# async def read_user_item(user_id: int, item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {'item_id': item_id, 'owner_id': user_id}
#     if q:
#         item.update({'q': q})
#     if not short:
#         item.update({'description': '描述'})
#     return item

'''
非路径查询参数，必须查询参数.needy必须传入值;skip 可以不传默认为0;limit可以不传，没有默认值
'''
@app.get('/items/{item_id}')
async def read_user_item(item_id: str,needy:str,skip:int =0,limit:Optional[int]=None):
    item={'item_id':item_id,'needy':needy,'skip':skip,'limit':limit}
    return item