from django.contrib import admin
from app01 import models

class UserInfoAdmin(admin.ModelAdmin):
    list_display=('username','age','email','phone')
admin.site.register(models.UserInfo,UserInfoAdmin)