from django.contrib import admin

from .models import biaoti,Article
class biaotiAdmin(admin.ModelAdmin):
    list_display = ('name','slug','intro')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','pub_date','update_time')

admin.site.register(biaoti,biaotiAdmin)
admin.site.register(Article,ArticleAdmin)
