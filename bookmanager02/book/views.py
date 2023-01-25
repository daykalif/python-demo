import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def demo(request):
    return HttpResponse('demodemo')


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


# http://127.0.0.1:8000/get_cookie/
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


"""
问题1：我换了浏览器，还能获取到session信息吗？
        - 不可以
        【暂不考虑下述情况：】
            跨浏览器Session获取：由于不同浏览器HttpSession不同，需要在服务端中增加一些代码，使得两个不同浏览器可以找到相同HttpSession
            具体做法是：
                - 当访问A页面时把HttpSession保存到全局map中，以HttpSession.getid()这个全局唯一字符串作为key，HttpSession作为Value，
                - B页面的url链接增加一个参数sid=HttpSession.getid()，服务端在解析b页面时取到sid的值，到全局map中找出HttpSession，这样A页面B页面可以使用相同HttpSession对象，然后再判定登录状态就不会有问题。
        
问题2：我不换浏览器，删除sessionid，则获取不到session数据
问题3：再去执行set_session的时候，会重新生成sessionid，session值超时会过期


保存在服务器的数据叫做session
    session需要依赖于cookie
    如果浏览器禁用了cookie，则session不能实现

    0.概念
    1.流程
        第一次请求：
            1⃣️ .我们第一次请求的时候可以携带一些信息（用户名/密码），cookie中没有任何信息
            2⃣️ .当我们的服务器接收到这个请求之后，进行用户名和密码的验证，验证没有问题可以设置session信息
            3⃣️ .在设置session信息的同时(session信息保存在服务器端)，服务器会在响应头中设置一个sessionid的cookie信息
            4⃣️ .客户端（浏览器）在接收到响应之后，会将cookie信息保存起来（保存sessionid的信息）
            
        第二次及其之后的请求：
            5⃣️ .第二次及其之后的请求都会携带session id信息
            6⃣️ .当服务器接收到这个请求之后，会获取到sessionid信息，然后进行验证，验证成功，则可以获取session信息（session信息保存在服务器端）
            
            
        在mysql中查看session信息：
            > mysql -uroot -proot
            > use book_42_02
            > show tables;
            > desc django_session;
            > select * from django_session;
    2.效果
        第一次请求：
             1⃣️ .第一次请求，在请求头中没有携带任何cookie信息
             2⃣️ .我们在设置session的时候，其实session做了2件事：
                    第一件：将数据保存在数据库中
                    第二件：设置一个cookie信息，这个cookie信息是以sessionid为key
                    cookie肯定会以响应的形式，在响应头中出现
        第二次及其之后的请求：
             3⃣️ .都会携带cookie信息，特别是sessionid
    3.从原理（http）角度
"""


# http://127.0.0.1:8000/set_session/?username=itcast&password=123
def set_session(request):
    """
    第一次请求：
        1⃣️ .我们第一次请求的时候可以携带一些信息（用户名/密码），cookie中没有任何信息
        2⃣️ .当我们的服务器接收到这个请求之后，进行用户名和密码的验证，验证没有问题可以设置session信息
        3⃣️ .在设置session信息的同时(session信息保存在服务器端)，服务器会在响应头中设置一个sessionid的cookie信息
        4⃣️ .客户端（浏览器）在接收到响应之后，会将cookie信息保存起来（保存sessionid的信息）
    """
    # 1.
    print(request.COOKIES)

    # 2.对用户名和密码进行验证
    # 假设认为用户名和密码正确
    user_id = 666

    # 3.设置session信息
    # request.session 理解为字典
    # 设置session的时候，其实session做了2件事：
    #     第一件：将数据保存在数据库中
    #     第二件：设置一个cookie信息，这个cookie信息是以sessionid为key
    request.session['user_id'] = user_id

    # 4.返回响应
    return HttpResponse('set_session')


# http://127.0.0.1:8000/get_session/
def get_session(request):
    """
    第二次及其之后的请求：
        5⃣️ .第二次及其之后的请求都会携带session id信息
        6⃣️ .当服务器接收到这个请求之后，会获取到sessionid信息，然后进行验证，验证成功，则可以获取session信息（session信息保存在服务器端）
    """

    # 1.第二次及其之后的请求都会携带session id信息
    print(request.COOKIES)

    # 2.当服务器接收到这个请求之后，会获取到sessionid信息
    # 进行验证，验证成功，则可以获取session信息（session信息保存在服务器端）

    # request.session 字典
    user_id = request.session['user_id']
    user_id = request.session.get('user_id')

    # 3.返回响应
    return HttpResponse('get_session')


"""
登陆页面
    GET请求是获取登陆的页面
    POST请求是验证登陆（用户名和密码是否正确）
"""


# GET请求是获取登陆的页面
def show_login(requset):
    return render(requset)


# POST请求是验证登陆（用户名和密码是否正确）
def veri_login(request):
    return redirect('首页')


# 我想有2个视图，变为1个视图
def login(request):
    # 我们需要区分业务逻辑
    if request.method == 'GET':
        # GET请求是获取登陆的页面
        return render(request)
    else:
        # POST请求是验证登陆（用户名和密码是否正确）
        return redirect('首页')


"""
面向对象
    类视图 是采用的面向对象的思路
    1.定义视图类
        1⃣️ .继承自View（from django.views import View）
        2⃣️ .不同的请求方式有不同的业务逻辑
            类视图的方法就直接采用http的请求名字作为我们的函数名.例如：get,post,put,delete...
        3⃣️ .类视图的方法的第二个参数，必须是请求实例对象
           类视图的方法必须有返回值，返回值是HttpResponse及其子类
    2.类视图的url引导
"""
from django.views import View


class BookView(View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')


class Person(object):
    # cls是谁？ --> Person类
    @classmethod
    def say(cls):
        pass

    # slef是谁？ --> 实例对象
    def eat(self):
        pass

    @staticmethod
    def run():
        pass


Person.say()
p = Person()
p.eat()

"""
个人中心页面
GET方式 展示 个人中心
POST实现个人中心信息的修改
定义视图类
"""
# http://127.0.0.1:8000/center/ --> 没有登陆信息，会跳转到http://127.0.0.1:8000/accounts/login/?next=/center/ 登陆界面
from django.contrib.auth.mixins import LoginRequiredMixin


class CenterView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse('个人中心展示')

    def post(self, request):
        return HttpResponse('个人中心修改')


##############################模板#######################################
# 3.定义视图
class HomeView(View):
    def get(self, request):
        # 1.获取数据
        username = request.GET.get('username')

        # 2.组织数据
        context = {
            'username': username,
            'age': 14,
            'birthday': datetime.now(),
            'friends': ['tom', 'jack', 'rose'],
            'money': {
                '2019': 12000,
                '2020': 18000,
                '2021': 25000,
            },
            'desc': '<script>alert("hot")</script>'
        }
        return render(request, 'index.html', context)
