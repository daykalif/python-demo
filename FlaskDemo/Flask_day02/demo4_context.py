from flask import Flask

# 请求上下文中的变量
from flask import request
from flask import session

# 应用上下文中的变量
from flask import current_app
from flask import g

app = Flask(__name__)


# 请求上下文中才可以使用request和session
# print(request.method)  # 只有在请求中才能使用request.method
# print(session.get('user_id', ''))  # 只有在请求中才能使用session    #当前用户存在服务器中的信息


# 应用上下文：只有应用运行起来之后才能使用current_app和g变量
# print(current_app.config.get('DEBUG'))


@app.route('/')
def index():
    print(request.method)
    print(current_app.config.get('DEBUG'))
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
