from django.db import models

# Create your models here.
"""
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

4.模型类需要继承自models.Model
5.模型类会自动为我们添加（生成）一个主键
6.属性名 = 属性类型(选项)
    属性名：不要使用python，mysql，class关键字
           不要使用连续的下划线(__)
    属性类型：和mysql的类型类似
    选项：CharField必须设置max_length
         null   是否为空
         unique 唯一
         default 设置默认值
         verbose_name 主要是 admin后台显示
           
"""

"""
书籍表：
    id,name,pub_data,readcount,commentcount,is_delete
"""


class BookInfo(models.Model):
    """
    1.主键 当前回自动生成
    2.属性复制过来就可以
    """

    # 属性名 = 属性类型(选项)
    name = models.CharField(max_length=10, unique=True)

    # 不要使用python，mysql，class关键字
    # class = models.CharField(max_length=10)

    # 不要使用连续的下划线
    # pub__data = models.CharField(max_length=10)

    # 发布日期
    pub_data = models.DateField(null=True)

    # 阅读量
    readcount = models.IntegerField(default=0)

    # 评论量
    commentcount = models.IntegerField(default=0)

    # 是否逻辑删除
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    # 性别
    gender = models.BooleanField()
    # 外键
    book = models.ForeignKey(BookInfo)
