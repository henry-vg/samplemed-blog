from django.contrib import admin
from blog.models import User, Keyword, Article, Comment

admin.site.register(User)
admin.site.register(Keyword)
admin.site.register(Article)
admin.site.register(Comment)