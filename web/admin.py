from django.contrib import admin
from web import models
# Register your models here.


class User(admin.ModelAdmin):
    list_display = ('id','username','token')
class Works(admin.ModelAdmin):
    list_display = ('uid','datetime', 'content')

admin.site.register(models.User,User)
admin.site.register(models.Works,Works)