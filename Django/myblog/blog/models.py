from django.db import models

"""
修改数据库模型后：
命令行中进行manage.py同级目录
执行python manage.py makemigrations app名（可选）
再执行python manage.py migrate
"""


class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    # pub_time = models.DateTimeField(auto_now=True)    # 添加当前时间
    pub_time = models.DateTimeField(null=True)      # 可修改时间

    def __str__(self):
        return self.title
