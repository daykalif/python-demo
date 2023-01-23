# GIT提交规范：

- feat或add：新功能
- update: 更新
- fix：修复的缺陷
- docs：文档
- style： UI样式
- refactor：代码重构
- test：增加测试
- chore：构建过程或辅助工具的变动

### Java或php的MVC模式:

M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作
V全拼为View，用于封装结果，生成页面展示的html内容
C全拼为Controller，用于接受请求，处理业务逻辑，与Model和View交互，返回结果

### Django的MVT模式：

M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理
V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答
T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html

1.安装django
2.安装虚拟环境：
sudo pip install virtualenv
sudo pip install virtualenvwrapper

3.

mkdir $HOME/.virtualenvs

4.vi ~/.bashrc

5.添加：
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

6.运行
source ~/.bashrc

7.创建虚拟环境 【python3为使用python3，py3_django_virtualenv_demo为虚拟环境名字】
mkvirtualenv -p python3 py3_django_virtualenv_demo

8.查看虚拟环境
workon

9.切换虚拟环境
workon py3_django_virtualenv_demo2

10.删除虚拟环境
rmvirtualenv py3_django_virtualenv_demo

10.不能删除正在使用的虚拟环境，需要退出
deactivate

11.在虚拟环境中安装django
pip install django==1.11.11

---
在虚拟环境中：
cd /Users/wangjiaping/work/project/server_learn/python/coding/DjangoDemo/bookmanager

### 创建Django项目

创建Django项目：【bookmanager为项目名称】

- django-admin startproject bookmanager

创建子应用：【login,pay,book为子应用名称】

- python manage.py startapp login
- python manage.py startapp pay
- python manage.py startapp book

在虚拟环境中：
cd /Users/wangjiaping/work/project/server_learn/python/coding/DjangoDemo/bookmanager
运行项目：
python manage.py runserver
更改端口号运行：
python manage.py runserver 127.0.0.1:8001

查看虚拟环境路径：
which python

给django项目设置解释器
Settings/python解释器选择python3.7(python3_django_42)

在下述文件中，安装/注册 子应用
/Users/wangjiaping/work/project/server_learn/python/coding/DjangoDemo/bookmanager/bookmanager/settings.py

在子应用的models中：
1.定义模型类
2.模型迁移
2.1 先生成迁移文件（不会在数据库中生成表，只会创建一个 数据表和模型的对应）
python manage.py makemigrations
2.2 再迁移（会在数据库中生成表）
python manage.py migrate
3.操作数据库

- 在哪里定义模型
- 模型继承自谁就可以
- ORM对应的关系
  表 --> 类
  对象 --> 数据行
  字段 --> 属性

#### pycharm使用DB Navigator插件连接虚拟db查看db.sqlite3文件，或者用Navicat打开查看

https://blog.csdn.net/nareta/article/details/106874963

### 运行项目：

在虚拟环境中：
cd /Users/wangjiaping/work/project/server_learn/python/coding/DjangoDemo/bookmanager
运行项目：
python manage.py runserver

### 1.访问后台登陆系统：

http://127.0.0.1:8000/admin/login/?next=/admin/

### 2.创建用户

创建账户密码：
cd /Users/wangjiaping/work/project/server_learn/python/coding/DjangoDemo/bookmanager
python manage.py createsuperuser
用户名：admin
密码：123456abc

### 3.注册模型【注意⚠️：需要将bookmanager设置为Sources Root】

在子应用的amin.py中注册模型

### 4.修改模型的方法

子应用models.py中返回内容

### 5.在子应用的view层，添加视图相关方法

### 6.定义路由

## 连接本地MySql

命令登陆：mysql -uroot -proot -h 127.0.0.1 --port 3306
创建数据库：create database book_42_01 charset utf8;
切换数据库：use book_42_01

在工程的settings.py中设置连接数据库

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # engine 引擎
        'POST': '127.0.0.1',  # 主机
        'PORT': '3306',  # 端口号
        'USER': 'root',  # 用户名
        'PASSWORD': 'root',  # 密码
        'NAME': 'book_42_01',  # 指定数据库
    }
}
```

修改过数据库字段或者内容后，需要更新数据库：
进入路径：/Users/wangjiaping/work/project/server_learn/python/coding/DjangoDemo/bookmanager
python manage.py makemigrations 【先生成迁移文件（不会在数据库中生成表，只会创建一个 数据表和模型的对应）】
python manage.py migrate 【再迁移（会在数据库中生成表）】

在终端mysql中此时：
show tables; # 查看所有数据表
desc bookinfo; # 查看bookinfo表信息

> 如果Mysql中没有tables，则运行上述的迁移;
> 或者运行下面代码

### bookinfo

```
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table    | Create Table                                                                                                                                                                                                                                                                                                                                               |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| bookinfo | CREATE TABLE `bookinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `commentcount` int(11) NOT NULL,
  `is_delete` tinyint(1) NOT NULL,
  `pub_date` date DEFAULT NULL,
  `readcount` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `book_bookinfo_name_d3d0edfe_uniq` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

### peopleinfo

```
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table      | Create Table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| peopleinfo | CREATE TABLE `peopleinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` smallint(6) NOT NULL,
  `book_id` int(11) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `book_peopleinfo_book_id_b216bb62_fk_book_bookinfo_id` (`book_id`),
  CONSTRAINT `book_peopleinfo_book_id_b216bb62_fk_book_bookinfo_id` FOREIGN KEY (`book_id`) REFERENCES `bookinfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
```

insert into bookinfo(name,pub_date,readcount,commentcount,is_delete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);

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

select * from bookinfo;
select * from peopleinfo;

### shell使用

类似于ipython的东西
python manage.py shell

> > > from book.models import BookInfo;
> > > BookInfo.objects.all();

### MySql忘记密码：

https://blog.csdn.net/qq_43674360/article/details/124758352

## 关于Mysql日志

```
一、查看日志是否开启：

1、show variables where Variable_name = 'general_log';

2、show variables like 'general_log';

二、开启和关闭的sql:
1、set global general_log=on;

2、set global general_log=off;

三、查看log文件所在位置：

1、show variables where Variable_name='general_log_file';

2、show variables like 'general_log_file';

四、修改log文件所在位置：

1、set global general_log_file='tmp/mysql_log.log';

五、日志输出类型table或file：

1、show variables like 'log_output';

六、修改日志输出类型：

1、set global log_output='table';

默认是FILE的方式，执行命令，修改成TABLE方式：

2、set global log_output='file'; --设置为行

一、查看慢查询设置：

1、show variables like "%slow%";

二、 启用慢查询（不建议使用）：

1、set global slow_query_log=ON;

2、set global slow_query_log=OFF;

三、 设置成2秒，加上global,下次进mysql已然生效：

1、set global long_query_time=2;

导出日志：

如果需要查询2017-09-17 07:21:09到2017-09-19 07:59:50 数据库为geeRunner 的操作日志，输入如下命令将数据写入到一个备用的txt即可

例：

mysqlbinlog --no-defaults --database=geeRunner --start-datetime="2017-09-17 07:21:09" --stop-datetime="2017-09-19 07:59:50" binlogs.000080 > sanjiaomao.txt

如果本地查询，输入命令：

 mysqlbinlog --no-defaults --database=geeRunner --start-datetime="2017-09-17 07:21:09" --stop-datetime="2017-09-19 07:59:50" binlogs.000080 | more

如果取下来查询，使用winscp工具，登录到db所在机器，将数据取出来。

如果需要过滤，只查询insert，update，delete的语句，可以这样写：

mysqlbinlog --no-defaults --database=raceEnroll  binlogs.000078 |grep update |more
————————————————
版权声明：本文为CSDN博主「提灯追影」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_63678046/article/details/126477515
```

### 查看mysql日志

sudo tail -f /usr/local/mysql/data/wangjiaingdeMBP.log


### shell 中查询：
```
>>> from book.models import BookInfo;
>>> books = BookInfo.objects.all();
>>> for book in books:
...     print(book);
... 
```

可在上述mysql日志查看中看见。