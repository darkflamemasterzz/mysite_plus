from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from . import forms  # 别忘了把 forms.py文件导入
# 导入models
from . import models     # 这个'.'是指上级目录



# Create your views here.


# 主页
def index(request):      # 通常将第一参数命名为request
    pass
    return render(request, 'login/index.html')   # render : 第二章 --> 视图函数及快捷方式 --> Django内置的快捷方法


# 登录
def login(request):
    # 判断用户是否已经登录
    if request.session.get('is_login', None):  # 这里get(is_login)的默认值是None
        # 当会话中间件启用后，传递给视图request参数的HttpRequest对象将包含一个session属性
        # 这个属性的值是一个类似字典的对象。
        return redirect("/index/")
    # 判断用户的请求方法是否为"POST"
    if request.method == "POST":      # login.html -- form表单的属性 -- method = 'POST'
        # (以下被注释的代码是为在html手动写的表单服务的)
        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)
        login_form = forms.UserForm(request.POST)
        message = "所有字段都必须填写！"
        # 确保用户名和密码都不为空
        if login_form.is_valid():
            # cleaned_data是一个字典类型数据: 根据key获得字典中的具体值
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                # 如果密码正确，则把key为is_login的值设为True
                # 并往session字典内写入用户状态和数据
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id   # 每一个表都默认有一个id吗 ？？
                    request.session['user_name'] = user.name  # user.name是 user表里的name属性的值
                    return redirect('/index/')
                else:
                    message = "密码不正确"
            except:
                message = "用户名不存在"
        # 如果验证不通过，则返回一个包含先前数据的表单给前端页面，方便用户修改
        return render(request, 'login/login.html', locals())  # locals(): 返回当前所有的本地变量字典
                                                              # message为什么会是字典？？
    # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据
    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


# 注册
def register(request):
    # 登录状态不允许注册。
    # 如果我想提醒用户在登录状态下不允许注册，要怎么做？？
    if request.session.get('is_login',None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)  # 感觉不合语法：为啥这个实例可以填写request.POST这个参数??
        message = "请填写查找内容!"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            # 判断两次输入的密码是否相同
            if password1 != password2:
                message = "两次输入的密码不同!"
                return render(request, 'login/register.html', locals())
            else:
                # 控制用户名唯一
                same_name_user = models.User.objects.filter(name=username)
                # User表里没有name为username的对象，则same_name_user的值为none(即False)
                if same_name_user:
                    message = '用户已经存在，请重新选择用户名!'
                    return render(request, 'login/register.html', locals())
                # 控制邮箱地址唯一
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 通过重重检查后，终于可以创建新用户了！
                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                # 这个save()操作容易漏掉
                new_user.save()
                # 注册完以后自动跳转到登录页面
                return redirect('/login/')
    # 如果没通过上面的检查，则“清空”一下register_form
    # 并重新注册
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())





# 登出
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")
