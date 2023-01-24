# 切换虚拟环境

> source ~/.bashrc

> workon

> workon python3_django_42

# 新建项目

> django-admin startproject bookmanager02

# 创建子应用

> django-admin startapp book

切换项目python Interpreter为python3.7(python3_django_42)

setting.py中注册子应用
'book.apps.BookConfig',

# 启动项目

> python manage.py runserver

# 在子应用的models.py中book定义模型

```
from django.db import models


# Create your models here.
# 准备书籍列表信息的模型表
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        # 修改数据库表名
        db_table = 'bookinfo'  # 指明数据库表名
        verbose_name = '图书'  # 在admin站点中显示的名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name
```

### 修改数据库(工程的settings.py文件中)

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # engine 引擎
        'POST': '127.0.0.1',  # 主机
        'PORT': '3306',  # 端口号
        'USER': 'root',  # 用户名
        'PASSWORD': 'root',  # 密码
        'NAME': 'book_42_02',  # 指定数据库
    }
}
```

### 在工程的__init__.py中引用mysql

```
import pymysql

pymysql.install_as_MySQLdb()
```

### mysql中创建

> create database book_42_02 charset utf8;

### 先生成迁移文件（不会在数据库中生成表，只会创建一个 数据表和模型的对应）

python manage.py makemigrations

### 再迁移（会在数据库中生成表）

python manage.py migrate

# 在子应用的models.py中people定义模型

```
# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        # 修改数据库表名
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

```

### 先生成迁移文件（不会在数据库中生成表，只会创建一个 数据表和模型的对应）

python manage.py makemigrations

### 再迁移（会在数据库中生成表）

python manage.py migrate

### Mysql中查看

> show databases;
> use book_42_02;
> show tables;

### 加入测试数据

```
insert into bookinfo(name,pub_date,readcount,commentcount,is_delete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);
```

```
insert into peopleinfo(name,gender,book_id,description,is_delete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('郭靖',1,1,'降龙十八掌',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);
```

### 定义book的视图 -- views.py

```
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('index')
```

### 新建book的urls

```
from django.conf.urls import url
from book.views import index

urlpatterns = [
    url(r'^home/$', index),
]
```

### 工程urls.py中设置路由

```
url(r'^', include('book.urls')),
```

### 利用HTTP协议向服务器传参途径

- 提取URL的特定不分，如/weather/beijing/2018，可以在服务器的路由中用正则表达式截取；
- 查询字符串（query string），形如key1=value1&key2=value2；
- 请求体（body）中发送的数据，比如表单数据、json、xml；
- 在http报文的头（header）中；


### debug模式运行Django
https://blog.csdn.net/DraGonBornCrash/article/details/80990458