from django.contrib import admin

from blog.models import Article


# 修改数据库模型后，将需要显示的字段加入到list_display中
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


admin.site.register(Article, ArticleAdmin)
