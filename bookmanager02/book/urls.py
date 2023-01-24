from django.conf.urls import url
from book.views import index

urlpatterns = [
    # name就是给url起一个名字
    # 我们可以通过name找到这个路由
    url(r'^home/$', index, name='adan'),
]
