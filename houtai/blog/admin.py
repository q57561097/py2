from django.contrib import admin

from .models import biaoti

class biaotiAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time')



admin.site.register(biaoti,biaotiAdmin)
