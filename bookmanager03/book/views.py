from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class SetSession(View):
    def get(self, request):
        # request.session = SessionStorage
        # 增加数据/修改数据
        request.session['name'] = 'itcast'

        # 删除某一个数据
        del request.session['name']

        # 删除session所有数据,会保留key
        request.session.clear()

        # 把数据库/redis中的key都删除了
        request.session.flush()

        # session是有时间的，默认是2周，
        # 我们可以设置时间
        # request.session.set_expiry(seconds)
        request.session.set_expiry(10)

        return HttpResponse('set session')


class GetSession(View):
    def get(self, request):
        # name = request.session['name']    # 当name不存在时，会报错
        name = request.session.get('name')
        print('name--->', name)
        return HttpResponse('get session')
