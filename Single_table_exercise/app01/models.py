from django.db import models


class UserInfo(models.Model):
    username=models.CharField(verbose_name='用户名',max_length=36)
    age=models.IntegerField(verbose_name='年龄')
    email=models.EmailField(verbose_name='邮箱')
    phone=models.IntegerField(verbose_name='电话号码')

