# FastAPI

### 安装
```
pip install fastapi 
pip install uvicorn #运行服务器
```
### 起步
> 1.创建一个FastAPI程序
```
from fastapi import FastAPI #导入FastAPI

app = FastAPI() #创建应用 app 可以自己命名

@app.get('/) #路径操作装饰器
def root(): #路径操作函数
  return {'message':'Hello FastAPI'}

#运行，命令行输入：uvicorn main:app --reload 
#参数说明：main是main.py app 是main.py中定义的应用名  --reload 是服务器重载，修改代码后自动重载
```
> 2.路径操作装饰器,必须跟着路径操作函数
  * @app.get()      -- 查询 select
  * @app.post()     -- 插入 insert
  * @app.put()      -- 修改 update
  * @app.delete()   -- 删除 delete
  * @app.options()
  * @app.head()
  * @app.patch()
  * @app.trace

> 3.路径操作函数，支持异步 函数开头使用async ,函数体使用await
  ```
  async def root():
    await...
  ```

### 路径参数