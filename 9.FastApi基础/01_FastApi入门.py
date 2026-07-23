from fastapi import FastAPI

# 创建 FastAPI 实例
app = FastAPI()


# 定义API接口 ---> 该函数的返回值表示API接口返回的数据
@app.get('/')
def root():
    return {"message": "Hello World"}


@app.get('/users')
def get_users():
    return [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]


# 启动FastApi（方式三）---> uvicorn: Python中的轻量级web服务器
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='01_FastApi入门:app', host='127.0.0.1', port=8000, reload=True)
