"""
中间件的作用：每次请求和响应的时候都会调用
中间件的定义
中间件的使用：我们可以判断每次请求中是否携带了cookie中某些信息
"""
from django.http import HttpResponse


def simple_middleware(get_response):
    # 这里是中间件第一次调用执行的地方
    print('init11111')

    def middleware(request):
        # 这里是 请求前
        print('before request1111111')
        username = request.COOKIES.get('username')
        print('username-->', username)
        if username is None:
            print('username is None')
            # return HttpResponse('哥们，你没有登陆诶')
        response = get_response(request)
        # 这里是 响应后/请求后
        print('after request/response11111111111')
        return response

    return middleware


def simple_middleware2(get_response):
    # 这里是中间件第一次调用执行的地方
    print('init22222')

    def middleware(request):
        # 这里是 请求前
        print('before request222222222')
        username = request.COOKIES.get('username')
        print('username-->', username)
        if username is None:
            print('username is None')
            # return HttpResponse('哥们，你没有登陆诶')
        response = get_response(request)
        # 这里是 响应后/请求后
        print('after request/response222222222')
        return response

    return middleware


"""
中间件的执行顺序：
before request1111111
before request222222222
after request/response222222222
after request/response11111111111

1.init的执行顺序官方没有特别说明
2.init执行了两次，是因为DEBUG = True（开启了debug模式）
3.init只会加载一次，清除控制台后，后续的请求便不会再打印
init22222
init11111
init22222
init11111
"""
