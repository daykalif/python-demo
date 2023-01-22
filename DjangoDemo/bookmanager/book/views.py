from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
from book.models import BookInfo

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

    # ------------------------------------------
    # name = '张三',
    # context = {
    #     'name': name
    # }
    # return render(request, 'index.html', context)
    # ------------------------------------------

    # 实现业务逻辑
    # 1.先把所有书籍查询出来
    # select * from bookinfo
    # ORM
    books = BookInfo.objects.all()
    # books = [BookInfo(),BookInfo()]
    # 2.组织数据
    context = {
        'books': books
    }
    return render(request, 'index.html', context)
    return HttpResponse('index')


"""
### shell使用
类似于ipython的东西
python manage.py shell

>>> from book.models import BookInfo;
>>> BookInfo.objects.all();
"""


##################################新增数据###########################################


from book.models import BookInfo

# 方式1
# 会把新生成的对象返回给我们
book = BookInfo(
    name='python',
    pub_date='2000-01-01'
)
# 需要手动调用save方法
book.save()

# 方式2 直接入库
# objects 模型的管理类
# 我们对模型的 增删改查 都找它
# 会把新生成的对象返回给我们
BookInfo.objects.create(
    name='java',
    pub_date='2010-01-01'
)


