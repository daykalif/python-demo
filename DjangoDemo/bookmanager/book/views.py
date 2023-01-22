from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

"""
视图
1.就是python函数
2.函数的第一个参数就是请求 和 请求相关的，它是HttpRequest的实例对象
3.我们必须要返回一个响应，响应是HttpRequest的实例对象或子类实例对象
"""


def index(request):
    # request, template_name, context = None
    # 参数1：当前请求
    # 参数2：模板文件
    # 参数3：context就是传递的参数

    name = '张三',
    context = {
        'name': name
    }
    return render(request, 'index.html', context)
    return HttpResponse('index')
