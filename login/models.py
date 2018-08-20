from django.db import models

# Create your models here.


# 创建User表
class User(models.Model):
    # 会与下面的sex联系上
    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)  # unique 表示并且唯一，也就是不能有相同姓名

    password = models.CharField(max_length=256)

    email = models.EmailField(unique=True)

    sex = models.CharField(max_length=32, choices=gender, default="男")

    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):    # 有什么作用？
        return self.name

    class Meta:          # 干什么用的
        # 用户按创建时间的反序排列，也就是最近的最先显示
        ordering = ["-c_time"]
        # 用于设置模型对象的直观、人类可读的名称。
        verbose_name = "用户"
        verbose_name_plural = "用户"
