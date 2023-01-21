from flask import Flask, session
from flask_script import Manager

app = Flask(__name__)

# 创建manager，与app进行关联
manager = Manager(app)


# 需求：可以通过命令在运行的时候指定运行的端口
# python demo5_script.py runserver -p 8888 -d


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()
