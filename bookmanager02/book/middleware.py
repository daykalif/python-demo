"""
中间件的作用：每次请求和响应的时候都会调用
中间件的定义
中间件的使用：我们可以判断每次请求中是否携带了cookie中某些信息
"""
from django.http import HttpResponse


def simple_middleware(get_response):
    def middleware(request):
        # 这里是 请求前
        print('before request1111111')
        username = request.COOKIES.get('username')
        print('username-->', username)
        if username is None:
            print('username is None')
            return HttpResponse('哥们，你没有登陆诶')
        response = get_response(request)
        # 这里是 响应后/请求后
        print('after request/response11111111111')
        return response

    return middleware
