## FastAPI（二）
### 请求体-字段
>1.基本示例
```
#请求体 字段检验使用Field
class Item(BaseModel):
    name: str
    #Field与Query、Path、Body相同
    description: Optional[str] = Field(None, title="标题", max_length=300)
    price: float = Field(..., gt=0, description="价格描述")
    tax: Optional[float] = None


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results

```
>2.请求体 字段子类型,List、Set
```
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    # tags: list = [] # 这个list没有类型
    # tags: List[str] = []#这个list必须都是str类型
    tags: Set[str] = set() #带类型的集合


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

```
>3.特殊类型、子模型、一组子模型
```
class Image(BaseModel):
    # url:str
    url:HttpUrl  #特殊类型，可以做有效性校验
    name:str

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []
    # image:Option[Image] =None #使用了其他的类模型(子模型)
    images:Optional[List[Image]]=None
# image:Option[Image] =None 请求体格式
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}


#images:Optional[List[Image]]=None 请求体格式
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
}

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

```
>4.深度嵌套模型
```

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    images: Optional[List[Image]] = None


class Offer(BaseModel):
    offerName: str
    offerDescription: Optional[str] = None
    offerPrice: float
    offerItems: List[Item]

#请求参数格式：
{
  "offerName": "string",
  "offerDescription": "string",
  "offerPrice": 0,
  "offerItems": [
    {
      "name": "string",
      "description": "string",
      "price": 0,
      "tax": 0,
      "tags": [],
      "images": [
        {
          "url": "string",
          "name": "string"
        }
      ]
    }
  ]
}

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

```

>5.列表类型、字典类型
```
class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):  # 纯列表请求体，支持编辑器自动提示
    for image in images:
        print(image.url)
    return images


@app.post('/index-weights/')
async def create_index_weights(weights: Dict[int, float]): #key 是int类型,value是float类型。json仅支持str作为键
    for weight in weights:
        print(type(weight))
    return weights

```

### 模式的额外信息 sechema Field Body
```

class Item(BaseModel):
    name: str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4) # Field额外信息
    tax: Optional[float] = Field(None, example=3.2)
    # schema额外信息
    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(
        ...,
        example={ #Body的额外信息
            "name": "Foo",
            "description": "A very nice Item",
            "price": 35.4,
            "tax": 3.2,
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
```
### 额外的数据类型
```

from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import Body, FastAPI

app = FastAPI()

# UUID:
# 一种标准的 "通用唯一标识符" ，在许多数据库和系统中用作ID。
# 在请求和响应中将以 str 表示。
# datetime.datetime:
# 一个 Python datetime.datetime.
# 在请求和响应中将表示为 ISO 8601 格式的 str ，比如: 2008-09-15T15:53:00+05:00.
# datetime.date:
# Python datetime.date.
# 在请求和响应中将表示为 ISO 8601 格式的 str ，比如: 2008-09-15.
# datetime.time:
# 一个 Python datetime.time.
# 在请求和响应中将表示为 ISO 8601 格式的 str ，比如: 14:23:55.003.
# datetime.timedelta:
# 一个 Python datetime.timedelta.
# 在请求和响应中将表示为 float 代表总秒数。
# Pydantic 也允许将其表示为 "ISO 8601 时间差异编码", 查看文档了解更多信息。
# frozenset:
# 在请求和响应中，作为 set 对待：
# 在请求中，列表将被读取，消除重复，并将其转换为一个 set。
# 在响应中 set 将被转换为 list 。
# 产生的模式将指定那些 set 的值是唯一的 (使用 JSON 模式的 uniqueItems)。
# bytes:
# 标准的 Python bytes。
# 在请求和相应中被当作 str 处理。
# 生成的模式将指定这个 str 是 binary "格式"。
# Decimal:
# 标准的 Python Decimal。
# 在请求和相应中被当做 float 一样处理。
@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
```

### Cookie和Header参数
```
from typing import Optional

from fastapi import FastAPI, Cookie,Header

app = FastAPI()

#Cookie参数，与Query、Path参数相同
@app.get('/items/')
# async def read_items(ads_id: Optional[str] = Cookie(None)):
async def read_items(ads_id: Optional[str] = Header(None)): #Header参数
    return {"ads_id": ads_id}
```

### 响应模型
>1.基本示例
```
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []

@app.post('/items/', response_model=Item) #response_model响应模型 返回的数据格式必须符合Item的要求
async def create_item(item: Item):
    return item
```
>2.响应模型与输入模型不同
```
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

@app.post('/user/', response_model=UserOut) #响应模型输出与请求数据模型不同，有效保证敏感数据
async def create_user(user: UserIn): #
    return user

```
>3.响应模型特殊处理
```

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

```