Java或php的MVC模式:
M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作
V全拼为View，用于封装结果，生成页面展示的html内容
C全拼为Controller，用于接受请求，处理业务逻辑，与Model和View交互，返回结果


Django的MVT模式：
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

7.创建虚拟环境  【python3为使用python3，py3_django_virtualenv_demo为虚拟环境名字】
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
