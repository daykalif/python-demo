安装django：python -m pip install Django
验证django是否安装成功：python -m django --version
创建项目：django-admin startproject myblog   # myblog为项目名称

# myblog项目中：
manage.py作用：
与项目进行交互的命令行工具集的入口
项目管理器

执行manage.py来查看所有命令,即python manage.py
django自带一个小型服务器：

运行项目：
    python manage.py runserver   
    或者  
    python manage.py runserver 9999   #（9999为端口号）
    
访问 http://127.0.0.1:9999/  或者  localhost:9999/即可
或者http://localhost:9999/index/

http://127.0.0.1:8000/blog/index/
http://127.0.0.1:8000/blog2/index/



wsgi.py作用：
WSGI（Python Web Server Gateway Interface）
中文名：Python服务器网关接口
Python应用与Web服务器之间的接口


urls.py作用：
URL配置文件
Django项目中所有地址（页面）都需要我们自己去配置其URL


settings.py作用：
项目的总配置文件
里面包含了数据库、Web应用、时间等各种配置


__init__.py的作用：
声明模块，一般文件为空，可以使该文件（如：myblog）成为一个模块，直接在代码中引用，
如：WSGI_APPLICATION = 'myblog.wsgi.application'，引用项目中的模块


创建应用：
打开命令行，进入项目中manage.py同级目录
命令行输入：python manage.py startapp blog    # blog为应用名称
添加应用名到settings.py中的INSTALLED_APPS里


# blog应用中：
migrations作用：
数据移植（迁移）模块
内容django自动生成

admin.py作用：
该应用的后台管理系统配置


apps.py作用：
该应用的一些配置
Django-1.9以后自动生成

models.py作用：
数据模块
使用ORM框架
类似于MVC结构中的Models（模型）


tests.py作用：
自动化测试模块
Django提供了自动化测试功能
在这里编写测试脚本（语句）


views.py作用：
执行相应的代码所在模块
代码逻辑处理的主要地点
项目中大部分代码均在这里编写


创建第一个页面（响应）
编辑blog.views
    每个响应对应一个函数，函数必须返回一个响应
    函数必须存在一个参数，一般约定为request
    每一个响应（函数）对应一个URL
    
编辑urls.py
    每个URL都以url的形式写出来
    url函数放在urlpatterns列表中
    url函数三个参数：URL（正则），对应方法，名称
    
    
第二种URL配置
    在根urls.py中引入include
    在APP目录下创建urls.py文件，格式与根urls.py相同
    根urls.py中url函数第二个参数改为include('blog.urls')
    注意事项：
    根urls.py针对APP配置的URL名称，是APP所有URL的总路径
    配置URL时注意正则表达式结尾符号$和/
    
    
Templates介绍
    HTML文件
    使用了Django模板语言（Django Template Language， DTL）
    可以使用第三方模板（如Jinja2）
    
    
开发第一个Template
    步骤：
        在APP的根目录下创建名叫Template的目录
        在该目录下创建HTML文件
        在views.py中返回render()
    DTL初步使用：
        render()函数中支持一个dict类型参数
        该字典是后台传递到模板的参数，键为参数名
        在模板中使用{{参数名}}来直接使用
    Django查找Template：
        Django按照INSTALLED_APPS中的添加顺序查找Templates
        不同APP下Templates目录的同名.html文件会造成冲突        
    解决Templates冲突方案：
        在APP的Templates目录下创建以APP名为名称的目录
        将html文件放入新创建的目录下 
    
Models介绍：
    通常，一个Model对应数据库的一张数据表
    Django中Models以类的形式表现
    它包含了一些基本字段以及数据的一些行为
    ORM：
        对象关系映射(Object Relation Mapping)
        实现了对象和数据库之间的映射
        隐藏了数据访问的细节，不需要编写SQL语句
    步骤：
        在应用根目录下创建models.py,并引入models模块
        创建类，继承models.Model,该类即是一张数据表
        在类中创建字段
        字段创建：
            字段即类里面的属性（变量）
            attr = models.CharField(max_length=64)
    生成数据表：
        步骤：
            命令行中进行manage.py同级目录
            执行python manage.py makemigrations app名（可选）
            再执行python manage.py migrate
        查看：
            Django会自动会在app/migrations/目录下生成移植文件
            执行python manage.py sqlmigrate 应用名 文件id 查看SQL语句
            (例如：python manage.py sqlmigrate blog 0001)
            默认sqlite3的数据库在项目根目录下db.sqlite3
        查看并编辑db.sqlite3
            使用第三方软件
            SQLite Expert Personal
            轻量级，完全免费
    页面呈现数据：
        后台步骤：
            views.py中import models
            article = models.Article.objects.get(pk=1)
            render(request,page,{'article':article})
        前端步骤：
            模板可直接使用对象以及对象的"."操作
        
        
Admin简介：
什么是Admin?
    Admin是Django自带的一个功能强大的自动化数据管理界面
    被授权的用户可直接在Admin中管理数据库
    Django提供了许多针对Admin的定制功能
            
配置Admin：
    Django提供admin后台，便于统一管理用户、权限和权限组，超级用户初始化方法
    创建用户初始化命令行：
    python manage.py createsuperuser    创建超级用户
    localhost：8000/admin/   Admin入口
    修改settings.py中LANGUAGE_CODE = 'zh_Hans'
    
    根据提示设置用户名、邮箱和密码：
    用户名 (leave blank to use 'admin'): admin
    电子邮件地址:
    Password: wangjiaping
    Password (again): wangjiaping
    密码长度太短。密码必须包含至少 8 个字符。
    这个密码太常见了。
    这个密码全部是数字的。
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    
    如果数据库出错：
    1. Delete your database
    2. python manage.py makemigrations
    3. python manage.py migrate
        
    配置应用：
        在应用下admin.py中引入自身的models模块（或里面的模型类）
        编辑admin.py：admin.site.register(models.Article)

使用Admin：
    修改数据：
        点击Article超链接进入Article列表页面
        点击任意一条数据，进入编辑页面修改
        编辑页面下方一排按钮可执行相应操作   
修改数据默认显示名称：
    步骤：
        在Article类下添加一个方法
        根据Python版本选择__str__(self)或__unicode_(self)
        return self.title       
    
模版For循环：
    {% for xx in xxs %}
    HTML语句
    {% endfor %}
    
博客文章页面：
    URL传递参数：
        参数写在响应函数中request后，可以有默认值
        URL正则表达式：r'^/article/(?P<article_id>[0-9]+)/$'
        URL正则中的组名必须和参数名一致
    
Django中的超链接：
    超链接目标地址：
        href后面是目标地址
        template中可以用"{% url 'app_name:url_name' param %}"
        其中app_name和url_name都在url中配置
    再配URL：
        url函数的名称参数：
            根urls，写在include()的第二个参数位置，namespace='blog'
            （如：myblog/myblog/urls.py下   ---   path('blog/', include('blog.urls', namespace='blog'))）
            应用下则写在url()的第三个参数位置，name='article'
            （如：myblog/blog/urls.py下 --- url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name="article_page")）
            主要取决于是否使用include引用了另一个url配置文件 
    
编辑响应函数：
    使用request.POST['参数名']获取表单数据
    models.Article.objexts.create(title,content)创建对象
    
    
Templates过滤器:（Django模版过滤器）
    什么是过滤器？
        写在模板中，属于Django模板语言
        可以修改模板中的变量，从而显示不同的内容
    怎么使用过滤器？
        {{ value | filter }}
        例子：{{ list_nums | length}}
        过滤器可叠加使用：{{ value | filter1 | filter2 | ... }}
        
Django Shell:
     什么是Django Shell？
        它是一个Python的交互式命令行程序
        它自动引入了我们的项目环境
        我们可以使用它与我们的项目进行交互
     如何使用Django Shell?
        python manage.py shell
        from blog.models import Article
        Article.objects.all()
     有什么用？
        我们可以使用Django shell来进行一些调试工作
        测试未知的方法       
        
        
Admin:
    创建admin配置类（如：修改blog/models.py）
        class ArticleAdmin(admin.ModelAdmin)
        注册：admin.site.register(Article,ArticleAdmin)
    显示其他字段：（如：修改blog/admin.py）
        list_display = ('title','content')
        list_display同时指出tuple和list
    过滤器：（Admin的过滤器）（如：修改blog/models.py）
    list_filter = ('pub_time',)
    