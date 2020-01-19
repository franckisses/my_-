from django.db import models

# Create your models here.


class UserProfile(models.Model):
    username = models.CharField(max_length=11,verbose_name='用户名',unique=True)
    phone = models.CharField(max_length=11,verbose_name='手机号')
    email = models.CharField(max_length=50,verbose_name='邮箱')
    password = models.CharField(max_length=32,verbose_name='密码')
    is_active = models.BooleanField(verbose_name='是否激活',default=0)
    # TODO 用户头像。用户签名 用户介绍