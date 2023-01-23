from django.conf.urls import url
from book.views import index

urlpatterns = [
    url(r'^home/$', index),
]
