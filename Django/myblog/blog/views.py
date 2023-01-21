from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    # 获取primary key=1的数据
    # article = models.Article.objects.get(pk=1)
    # return render(request, 'blog/index.html', {'hello': 'Hello Bolg!!!', 'article': article})

    # 获取所有数据,返回一个查询的集合
    articles = models.Article.objects.all()

    # return HttpResponse("Hello world")
    return render(request, 'blog/index.html', {'hello': 'Hello Bolg!!!', 'articles': articles})


def article_page(request, article_id):
    articlePage = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article_page': articlePage})


# 第二步：在views.py中编写后端响应
# 第七步：添加参数article_id，编辑和新建都需要使用
def edit_page(request, article_id):
    # 新建
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    # 编辑
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


# 第四步：获取请求过来的参数并创建文章，保存下来，成功返回到主页
def edit_action(request):
    title = request.POST.get('title', 'TITLE')  # 第二个值'TITLE'为默认值
    content = request.POST.get('content', 'CONTENT')
    # 第十二步：
    article_id = request.POST.get('article_id', '0')
    # 创建文章
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article_page': article})
