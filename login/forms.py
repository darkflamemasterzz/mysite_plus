# Django的表单给我们提供了下面三个主要功能：
#   准备和重构数据用于页面渲染；
#   为数据创建HTML表单元素；
#   接收和处理用户从表单发送过来的数据。

#   form表单中的一个字段代表<form>中的一个<input>元素。

from django import forms
from captcha.fields import CaptchaField


# 登录(login)表单
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)  # 这里面的参数名我可以更改吗？
    # widget是字段的一个内在属性，用于定义字段在浏览器的页面里以何种HTML元素展现
    # widget:在form表单里表现为<input type='password' />
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
    captcha = CaptchaField(label='验证码')  # CaptchaField不需要与Form有联系吗?


# 注册(register)表单
class RegisterForm(forms.Form):
    gender =(
        ('male', "男"),
        ('female', "女"),
    )
    # 尝试吧widget换成不同的类型看看？？
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))  # 这里attrs的作用是??
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')
