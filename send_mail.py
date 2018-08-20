
#  运行不了 还未搞懂
#  运行不了 还未搞懂
#  运行不了 还未搞懂

import os   # 干什么用的??
from django.core.mail import send_mail

# 由于这里是单独运行send_mail.py文件，所以无法使用Django环境，需要通过os模块对环境变量进行设置
# 如果是这样，那为什么不把它设置在mysite_plus.mysite_plus或者login里头呢？？
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite_plus.settings'  # ??陌生??


if __name__ == '__main__':    # 这啥玩意儿？？

    send_mail(
        '测试邮件的标题',
        '测试邮件的内容',
        '13678954738test@sina.com',  # 邮件发送方
        ['13678954738@163.com'],   # 邮件接收方
    )

#  运行不了 还未搞懂
#  运行不了 还未搞懂
#  运行不了 还未搞懂