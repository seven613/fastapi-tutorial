from typing import Optional, List, Set, Dict
from pydantic import BaseModel, Field, HttpUrl

from fastapi import FastAPI,  Body

app = FastAPI()


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
