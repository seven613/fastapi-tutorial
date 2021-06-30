from typing import Optional

from fastapi import FastAPI, Cookie,Header

app = FastAPI()

#Cookie参数，与Query、Path参数相同
@app.get('/items/')
# async def read_items(ads_id: Optional[str] = Cookie(None)):
async def read_items(ads_id: Optional[str] = Header(None)): #Header参数
    return {"ads_id": ads_id}
