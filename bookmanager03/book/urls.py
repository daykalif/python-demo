from django.conf.urls import url
from book.views import SetSession, GetSession

urlpatterns = [
    url(r'^set_session/', SetSession.as_view()),
    url(r'^get_session/', GetSession.as_view()),
]
