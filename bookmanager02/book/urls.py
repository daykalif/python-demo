from django.conf.urls import url
from book.views import index, detail

urlpatterns = [
    # name就是给url起一个名字
    # 我们可以通过name找到这个路由
    url(r'^home/$', index, name='adan'),

    # http://127.0.0.1:8000/category_id/book_id/
    # 通过分组来获取正则中的数据
    # 我们进行正则分组的参数会传递给视图，定义视图的时候需要定义变量来接收参数
    url(r'^(\d+)/(100)/$', detail),
]
