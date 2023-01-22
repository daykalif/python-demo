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

##################################修改数据###########################################

from book.models import BookInfo

# 方式1
# 1.查询数据
# select * from bookinfo where id=1
book = BookInfo.objects.get(id=1)

# 2.直接修改实例的属性
book.readcount = 20

# 3.需要手动调用save方法
book.save()

# 方式2 直接更新
# filter 过滤
BookInfo.objects.filter(id=1).update(
    readcount=100,
    commentcount=200
)

##################################删除数据###########################################

# 方式1：（直接删除）
# 1.先查询出数据
book = BookInfo.objects.get(id=5)
# 2.调用删除方法
book.delete()

# 方式2：（直接删除）
BookInfo.objects.filter(id=9).delete()

##################################基本查询###########################################

# get 得到某一个数据 --> get得到的是单一对象
# all 获取所有的
# count 个数

# select * from bookinfo where id=1
# 返回一个对象
book = BookInfo.objects.get(id=1)

# 查询id 不存在的数据会抛出异常
book = BookInfo.objects.get(id=100)
"""
book.models.DoesNotExist: BookInfo matching query does not exist.
"""

try:
    book = BookInfo.objects.get(id=2)
# except Exception as e:
#     print(e)
except BookInfo.DoesNotExist:
    pass

# all --> all 返回所有结果，是列表
BookInfo.objects.all()

# 获取count的两种方式：
BookInfo.objects.all().count()
BookInfo.objects.count()

##################################filter,get,exclude###########################################


"""
select xxx from bookinfo where 条件语句
相当于 where查询

filter  :   筛选/过滤 返回n个结果（n=0/1/n）
get     :           返回1个结果
exclude :   排除掉符合条件剩下的结果 相当于 not

语法形式：
    以 filter(字段名__运算符=值) 为例
"""

# --------------------------------查询编号为1的图书-------------------------------
# exact 精确的 准确的 就是等于
BookInfo.objects.get(id__exact=1)
# 习惯使用下述简写形式
BookInfo.objects.get(id=1)

# 返回结果：<BookInfo: 射雕英雄传>    --->    get返回的是一个单一对象

# 通过filter获取
BookInfo.objects.filter(id__exact=1)
# 返回结果：<QuerySet [<BookInfo: 射雕英雄传>]>    --->    filter返回的是一个列表

# --------------------------------查询书名包含'湖'的图书-------------------------------
# contains 包含
BookInfo.objects.filter(name__contains='湖')

# --------------------------------查询书名以'部'结尾的图书-------------------------------
BookInfo.objects.filter(name__endswith='部')

# --------------------------------查询书名为空的图书-------------------------------
BookInfo.objects.filter(name__isnull=True)

# --------------------------------查询编号为1或3或5的图书-------------------------------
BookInfo.objects.filter(id__in=[1, 3, 5])

# --------------------------------查询编号大于3的图书-------------------------------
# gt    大于
# gte   大于等于
# lt    小于
# lt3    小于等于
BookInfo.objects.filter(id__gt=3)

# --------------------------------查询书籍id不为3的图书-------------------------------
BookInfo.objects.exclude(id__exact=3)
BookInfo.objects.exclude(id=3)

# --------------------------------查询1980年发布的图书-------------------------------
BookInfo.objects.filter(pub_date__year='1980')

# --------------------------------查询1990年1月1日后发布的图书-------------------------------
BookInfo.objects.filter(pub_date__gt='1990-1-1')
# BookInfo.objects.filter(pub_date__gt='1990/1/1')  不正确


##################################F###########################################

# 两个属性怎么比较 F对象
"""
F对象的语法形式

filter(字段名__运算符=F('字段名'))
"""
from django.db.models import F

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 查询阅读量大于等于评论量2倍的图书
BookInfo.objects.filter(readcount__gte=F('commentcount') * 2)
