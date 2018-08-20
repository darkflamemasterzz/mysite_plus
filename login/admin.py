from django.contrib import admin

# Register your models here.

from . import models

# 注册User表
admin.site.register(models.User)
