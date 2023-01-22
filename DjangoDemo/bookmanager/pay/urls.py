from pay.views import order
from django.conf.urls import url

urlpatterns = [
    # pay/order/
    # 正则需要匹配：order/
    url(r'^order/$', order),
]
