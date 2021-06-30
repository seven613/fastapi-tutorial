from typing import Optional
from pydantic import BaseModel, Field

from fastapi import FastAPI,  Body

app = FastAPI()


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
