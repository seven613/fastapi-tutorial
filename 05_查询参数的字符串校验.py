from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI, Query

app = FastAPI()

'''
参数校验，使用Query
'''


@app.get('/items/')
# 字符串不为空时，最短3个字符，最长18个字符。regex使用正则表达式
# title 标题名，description：描述, alias 别名，deprecated 弃用函数
async def read_item(q: Optional[str] = Query(None, title="查询字符串", description='描述', alias='itemp-query',deprecated=True,min_lenght=3, max_length=50, regex='^fixedquery$')):
    result = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        result.update({'q': q})
    return result
