from django.conf.urls import url
from book.views import SetSession

urlpatterns = [
    url(r'^set_session/', SetSession.as_view()),
]
