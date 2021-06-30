from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# #定义入口数据模型类
# class UserIn(BaseModel):
#     username: str
#     password: str #明文
#     email: EmailStr
#     full_name: Optional[str] = None

# #定义出口数据模型类，没有密码
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# #定义数据库数据模型类
# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str#哈希之后的密码
#     email: EmailStr
#     full_name: Optional[str] = None

# #明文密码哈希
# def fake_password_hasher(raw_password: str):
#     return "supersecret"+raw_password

# #保存到数据库
# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)#**user_in.dict()解包，然后再由UserInDB封装成对象
#     print("User Saved!....")
#     return user_in_db

# @app.post('/user/',response_model=UserOut)
# async def create_user(user_in:UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

#简化代码
class UserBase(BaseModel):
    username:str
    email:EmailStr
    full_name:Optional[str]=None

class UserIn(UserBase):
    password:str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password:str

#明文密码哈希
def fake_password_hasher(raw_password: str):
    return "supersecret"+raw_password

#保存到数据库
def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)#**user_in.dict()解包，然后再由UserInDB封装成对象
    print("User Saved!....")
    return user_in_db

@app.post('/user/',response_model=UserOut)
async def create_user(user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved