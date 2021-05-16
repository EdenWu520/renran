from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    avatar = models.ImageField(upload_to='avatar', verbose_name='头像', null=True)
    wxchat = models.CharField(max_length=100, null=True, unique=True, verbose_name="微信账号")
    alipay = models.CharField(max_length=100, null=True, unique=True, verbose_name="支付宝账号")
    qq_number = models.CharField(max_length=11, null=True, unique=True, verbose_name="QQ号")

    class Meta:
        db_table = "rr_users"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username if self.username else "暂无"

