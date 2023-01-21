import json

from flask import Flask, request, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    return 'demo1'


# 给路由添加参数，格式就是<参数名>
# 并且试图函数需要接收这个参数
# 默认请求方式：get
@app.route('/user/<int:user_id>')   # int默认是指integer转换器
def demo2(user_id):
    return 'demo2 %s' % user_id


@app.route('/demo3', methods=['GET', 'POST'])  # methods中大小写没关系
def demo3():
    return 'demo3 %s' % request.method


@app.route('/json11111')
def demo4():
    json_dict = {
        "name": "zhangsan",
        "age": 19
    }
    # 使用JSON.dumps将字典转成JSON字符串
    result = json.dumps(json_dict)

    # 使用JSON.loads将JSON字符串转成字典
    # test_dict = json.loads('{"age":18,"name":"laowang"}')

    # return result  # Content-Type: text/html; charset=utf-8
    # jsonify会指定响应内容的数据格式（告诉客户端我返回给你的数据格式是什么）
    return jsonify(json_dict)  # Content-Type: application/json


@app.route('/redirect')
def demo5():
    # return redirect('http://www.itheima.com')   # 重定向到黑马

    # 重定向到自己写的试图函数
    # url_for:取到指定试图函数所对应的路由URL，并且可以携带参数
    # return redirect('/user/123')
    # return redirect(url_for('demo1'))
    return redirect(url_for('demo2', user_id=123))


# 返回自定义的状态码
@app.route('/demo6')
def demo6():
    return '状态码为666：表示当前已经晚上10点了', 666


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
