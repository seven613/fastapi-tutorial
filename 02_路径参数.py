from enum import Enum
from fastapi import FastAPI

app = FastAPI()


# item_id是路径参数，是个变量，必须使用{}包裹。请求完整路径:http://127.0.0.1:8000/items/foo,其中foo是参数
# @app.get('/items/{item_id}')
# # async def read_item(item_id):  # item_id必须与路径参数一致
# #     return {'item_id': item_id}
# async def read_item(item_id: int):  # 路径参数带有类型
#     return {'item_id': item_id}


# '''
# /users/me 必须在/users/{user_id} 前面，
#   因为代码是顺序执行，放在后面/users/me 就被覆盖了
#   me 会当成 user_id传进去，匹配read_user这个函数
# '''
# @app.get('/users/me')
# async def read_user_me():
#     return{"user_id": 'the current_user'}


# @app.get('/users/{user_id}')
# async def read_user(user_id: str):
#     return{"user_id": user_id}

# '''
# 定义模型类，
# API 文档将能够知道这些值必须为 string 类型并且能够正确地展示出来
# 然后创建具有固定值的类属性，这些固定值将是可用的有效值：
# '''
# class ModelName(str, Enum): #创建一个继承自 str 和 Enum 的子类。通过从 str 继承，
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName): #类型标注为ModelName类型
#     if model_name == ModelName.alexnet:
#       #model_name.alexnet.value 获取枚举类型的值
#         return{"model_name": model_name,"model_name.alexnet.value":model_name.alexnet.value, "message": "Deep Learning FTW"}

#     if model_name == ModelName.lenet:
#         return{"model_name": model_name, "message": "leCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}

'''
路径参数包含路径，如/files/{file_path},file_path='home/johndoe/myfile.txt'
必须使用file_path:path，:path说明应该匹配路径，测试后发现也可以匹配字符串
'''
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
