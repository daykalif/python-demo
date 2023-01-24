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
