from django.contrib import admin

# Register your models here.
from book.models import BookInfo

admin.site.register(BookInfo)
