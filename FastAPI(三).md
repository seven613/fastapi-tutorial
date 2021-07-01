### Form
```
@app.post('/login/')
async def login(*, username: str = Form(...), password: str = Form(...)):
    return{"username": username}

```

### 数据转为JSON
```
@app.put('/items/{id}')
async def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item) #将数据转为JSON格式
    return(json_compatible_item_data)

```