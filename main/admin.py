from django.contrib import admin
from .models import Category, News, NewsImage, NewsCulture, NewsSport

admin.site.register(Category)
admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(NewsCulture)
admin.site.register(NewsSport)

