from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


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
