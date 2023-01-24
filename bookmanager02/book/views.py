import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def index(request):
    """
    reverse 就是通过name来动态获取路径（路由）
    如果没有设置了namespace，则可以通过name来获取reverse(name)
    如果设置了namespace，这个时候就需要通过namespace:name来获取reverse(namespace:name)

    登陆成功之后需要跳转到首页
    注册成功之后需要跳转到首页
    """

    # viewname 通过视图名字
    # path = reverse('adan')
    # print(path)

    # 如果我们设置了namespace，这个时候就需要通过namespace:name来获取路由
    path = reverse('book:adan')
    print(path)

    # 跳转页面
    # 登陆成功之后需要跳转到首页
    # return redirect('/index/')
    # return redirect(path)

    # 注册成功之后需要跳转到首页
    # return redirect('/index/')
    # return redirect(path)

    return HttpResponse('index')


"""
GET方式
"""
# def detail(request, category_id, book_id):
#     # 1/100/
#     print(category_id, book_id)
#
#     ####################################查询字符串#######################################
#     """
#     # http://yun.itheima.com/course/936.html?capid=1&hm=2
#     以?作为一个分隔
#     ?前面表示路由
#     ?后面表示get方式传递的参数 称之为 查询字符串
#     ?key=value&key=value...
#
#     我们在登陆的时候会输入用户名和密码 理论上 用户名和密码都应该以POST方式进行传递；
#     为了理解GET方式，用用户名和密码进行示例，访问：
#     http://127.0.0.1:8000/1/200?username=itcast&password=123
#     """
#     query_params = request.GET
#     print(query_params)  # <QueryDict: {'username': ['itcast'], 'password': ['123']}>
#
#     username = query_params['username']
#     password = query_params.get('password')
#     # print(username, password)     # itcast    123
#
#     """
#     http://127.0.0.1:8000/1/200?username=itcast&username=itheima&password=123
#
#     # QueryDict 以普通的字典形式来获取 一键多值的时候，只能获取最后的那一个值
#     # 我们想获取一键一值的话，需要使用 QueryDict 的get方法
#     # 我们想获取一键多值的话，需要使用 QueryDict 的list方法
#     """
#     query_params = request.GET
#     print(query_params)  # <QueryDict: {'username': ['itcast', 'itheima'], 'password': ['123']}>
#     username = query_params['username']
#     password = query_params.get('password')
#     # print(username, password)     # itheima    123
#
#     users = query_params.getlist('username')
#     print(users)  # ['itcast', 'itheima']
#
#     return HttpResponse('detail')


"""
POST方式
"""


#
# ####################################POST表单数据#######################################
# def detail(request, category_id, book_id):
#     data = request.POST
#     print(data)  # <QueryDict: {'username': ['itheima'], 'password': ['123']}>
#
#     return HttpResponse('detail')

# ####################################POST JSON数据#######################################
# def detail(request, category_id, book_id):
#     """ JSON用的是双引号
#     {
#         "username":"itcast",
#         "password":123
#     }
#     """
#     body = request.body
#     print(body)  # b'{\n    "username": "itcast",\n    "password": 123\n}'
#     body_str = body.decode()
#     print(body_str)  # JSON形式的字符串
#     # {
#     #     "username": "itcast",
#     #     "password": 123
#     # }
#
#     """
#     json
#     json.dumps  将字典转化为JSON形式的字符串
#     json.loads  将JSON形式的字符串转化为字典
#     """
#
#     data = json.loads(body_str)
#     print(data)  # {'username': 'itcast', 'password': 123}
#
#     return HttpResponse('detail')


# ####################################请求头#######################################
# def detail(request, category_id, book_id):
#     print(request.META)
#
#     content_type = request.META['CONTENT_TYPE']
#     print(content_type)
#
#     print(request.method)
#     return HttpResponse('detail')


# ####################################HttpResponse#######################################
# def detail(request, category_id, book_id):
#     data = {'name': 'itcast'}
#     # HttpResponse
#     # 第一个参数：content         传递字符串，不要传递对象，字典等数据
#     # 第二个参数：statue          HTTP status code must be an integer from 100 to 599.（只能使用系统规定的）
#     # 第三个参数：content_type    是一个MIME类型
#     #                           语法形式是：大类/小类
#     #                           text/html   text/css    text/javascript
#     #                           application/json
#     #                           image/png   image/gif   image/gif
#
#     return HttpResponse(data, status=400)     # 此处的data就是展示给页面的字符串信息


####################################JsonResponse#######################################
def detail(request, category_id, book_id):
    from django.http import JsonResponse

    data = {'name': 'itcast'}
    return JsonResponse(data, status=400)


"""
保存在客户端的数据叫做cookie
    cookie是保存在客户端的
    cookie是基于域名（IP）的
    0.概念
    1.流程
        第一次请求过程
        1⃣️ .我们的浏览器第一次请求服务器的时候，不会携带任何cookie信息
        2⃣️ .服务器接收到请求之后，发现 请求中没有任何cookie信息
        3⃣️ .服务器设置一个cookie，这个cookie设置在响应中
        4⃣️ .我们的浏览器接收到这个响应之后，发现响应中有cookie信息，浏览器会将cookie信息保存起来
        
        第二次及其之后请求过程
        5⃣️ .当我们的浏览器第二次及其之后的请求都会携带cookie信息
        6⃣️ .我们的服务器接收到请求之后，会发现请求中携带cookie信息，这样的话就认识是谁的请求了
    2.看效果
    3.从http协议角度，深入掌握cookie的流程（原理）
        第一次
             1⃣️ .我们是第一次请求服务器，不会携带任何cookie信息，请求头中没有任何cookie信息
             2⃣️ .服务器会响应设置cookie信息，响应头中有set_cookie信息
        
        第二次
             3⃣️ .我们第二次及其之后的请求都会携带cookie信息，请求头中有cookie信息
             4⃣️ .（可选）在我们当前的代码中，没有再 在响应头中设置cookie，所以响应头中有set_cookie信息

保存在服务器的数据叫做session
"""


# 访问：http://127.0.0.1:8000/set_cookie/?username=itcast
def set_cookie(request):
    """
        第一次请求过程
        1⃣️ .我们的浏览器第一次请求服务器的时候，不会携带任何cookie信息
        2⃣️ .服务器接收到请求之后，发现 请求中没有任何cookie信息
        3⃣️ .服务器设置一个cookie，这个cookie设置在响应中
        4⃣️ .我们的浏览器接收到这个响应之后，发现响应中有cookie信息，浏览器会将cookie信息保存起来
    """
    # 1.先判断有没有cookie信息【先假设没有】

    # 2.获取用户名
    username = request.GET.get('username')

    # 3.因为我们假设没有cookie信息，我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')
    # key,value
    # max_age 单位是秒，时间是从服务器接收到这个请求时间 + 秒数 计算之后的时间
    response.set_cookie('username', username, max_age=3600)

    # 删除cookie的两种方式
    # response.delete_cookie(key)
    # response.set_cookie(key, value, max_age=0)

    # 4.返回响应
    return response


def get_cookie(request):
    """
    第二次及其之后请求过程
    5⃣️ .当我们的浏览器第二次及其之后的请求都会携带cookie信息
    6⃣️ .我们的服务器接收到请求之后，会发现请求中携带cookie信息，这样的话就认识是谁的请求了

    """
    # 1.服务器可以接收（查看）cookie信息
    cookies = request.COOKIES

    # cookies 就是一个字典
    username = cookies.get('username')

    # 2.得到用户信息就可以继续其他的业务逻辑了
    return HttpResponse('get_cookie')  # 此处的'get_cookie'就是展示给页面的字符串信息
