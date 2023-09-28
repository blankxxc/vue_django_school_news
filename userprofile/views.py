from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm
from comment.models import Comment
# 引入 UserRegisterForm 表单类
from .forms import UserLoginForm, UserRegisterForm

from new.models import  news,Tag
# Create your views here.


# 用户登录
def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            # .cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # 检验账号、密码是否正确匹配数据库中的某个用户
            # 如果均匹配则返回这个 user 对象
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                
                # 将用户数据保存在 session 中，即实现了登录动作
                login(request, user)

                new = news.objects.all().reverse()[:5]
                tui1 = news.objects.order_by('tui')[0]
                tui2 = news.objects.order_by('tui')[1]
                xuexiao_qian = news.objects.order_by('-created_time').filter(tags__name="学校")[0]
                xuexiao_hou = news.objects.order_by('-created_time').filter(tags__name="学校")[1:4]
                dangwu_qian = news.objects.order_by('-created_time').filter(category__name="党务工作")[0]
                dangwu_hou = news.objects.order_by('-created_time').filter(category__name="党务工作")[1:4]
                xueshu_qian = news.objects.order_by('-created_time').filter(category__name="学术交流")[0]
                xueshu_hou = news.objects.order_by('-created_time').filter(category__name="学术交流")[1:4]
                bisai_qian = news.objects.order_by('-created_time').filter(category__name="各类赛事")[0]
                bisai_hou = news.objects.order_by('-created_time').filter(category__name="各类赛事")[1:4]
                suzhi_qian = news.objects.order_by('-created_time').filter(category__name="素质教育")[0]
                suzhi_hou = news.objects.order_by('-created_time').filter(category__name="素质教育")[1:4]
                qita_qian = news.objects.order_by('-created_time').filter(category__name="其他")[0]
                qita_hou = news.objects.order_by('-created_time').filter(category__name="其他")[1:4]
                redian = news.objects.order_by('-views')[:4]
                zuixin = news.objects.order_by('-created_time')[:4]
                pinglun = Comment.objects.order_by('-created')[:4]
                tuijian = news.objects.order_by('tui')[:4]

                context = {
                'news': new,
                'tui1':tui1,
                'tui2':tui2,
                'xuexiao_qian':xuexiao_qian,
                'xuexiao_hou':xuexiao_hou,
                'dangwu_qian':dangwu_qian,
                'dangwu_hou':dangwu_hou,
                'xueshu_qian':xueshu_qian,
                'xueshu_hou':xueshu_hou,
                'bisai_qian':bisai_qian,
                'bisai_hou':bisai_hou,
                'suzhi_qian':suzhi_qian,
                'suzhi_hou':suzhi_hou,
                'qita_qian':qita_qian,
                'qita_hou':qita_hou,
                'redian' :redian,
                'zuixin' :zuixin,
                'pinglun' :pinglun,
                'tuijian' :tuijian

                }
                return render(request, 'news/index.html', context)
            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = { 'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


# 用户注册
def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_register_form.cleaned_data['password'])
            new_user.save()
            # 保存好数据后立即登录并返回博客列表页面
            login(request, new_user)
            return render(request, 'userprofile/login.html')
        else:
            return HttpResponse("注册表单输入有误。请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = { 'form': user_register_form }
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")



# 用户退出
def user_logout(request):
    logout(request)
    new = news.objects.all().reverse()[:5]
    tui1 = news.objects.order_by('tui')[0]
    tui2 = news.objects.order_by('tui')[1]
    xuexiao_qian = news.objects.order_by('-created_time').filter(tags__name="学校")[0]
    xuexiao_hou = news.objects.order_by('-created_time').filter(tags__name="学校")[1:4]
    dangwu_qian = news.objects.order_by('-created_time').filter(category__name="党务工作")[0]
    dangwu_hou = news.objects.order_by('-created_time').filter(category__name="党务工作")[1:4]
    xueshu_qian = news.objects.order_by('-created_time').filter(category__name="学术交流")[0]
    xueshu_hou = news.objects.order_by('-created_time').filter(category__name="学术交流")[1:4]
    bisai_qian = news.objects.order_by('-created_time').filter(category__name="各类赛事")[0]
    bisai_hou = news.objects.order_by('-created_time').filter(category__name="各类赛事")[1:4]
    suzhi_qian = news.objects.order_by('-created_time').filter(category__name="素质教育")[0]
    suzhi_hou = news.objects.order_by('-created_time').filter(category__name="素质教育")[1:4]
    qita_qian = news.objects.order_by('-created_time').filter(category__name="其他")[0]
    qita_hou = news.objects.order_by('-created_time').filter(category__name="其他")[1:4]
    redian = news.objects.order_by('-views')[:4]
    zuixin = news.objects.order_by('-created_time')[:4]
    pinglun = Comment.objects.order_by('-created')[:4]
    tuijian = news.objects.order_by('tui')[:4]

    context = {'news': new,
    'tui1':tui1,
    'tui2':tui2,
    'xuexiao_qian':xuexiao_qian,
    'xuexiao_hou':xuexiao_hou,
    'dangwu_qian':dangwu_qian,
    'dangwu_hou':dangwu_hou,
    'xueshu_qian':xueshu_qian,
    'xueshu_hou':xueshu_hou,
    'bisai_qian':bisai_qian,
    'bisai_hou':bisai_hou,
    'suzhi_qian':suzhi_qian,
    'suzhi_hou':suzhi_hou,
    'qita_qian':qita_qian,
    'qita_hou':qita_hou,
    'redian' :redian,
    'zuixin' :zuixin,
    'pinglun' :pinglun,
    'tuijian' :tuijian

    }

    return render(request, 'news/index.html', context)
