from django.contrib import admin
from blog.models import Keyword, Article, Comment

admin.site.register(Keyword)
admin.site.register(Article)
admin.site.register(Comment)
