from django.shortcuts import render, HttpResponse
from .models import Tag, news
from django.views.generic import View, ListView
from comment.models import Comment
from numpy import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def new_list(request):
    try:

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
        'tui1':tui1,'tui2':tui2,
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

        # render函数：载入模板，并返回context对象
        return render(request, 'news/index.html', context)

    except:
        return HttpResponse("没有找到数据！!")



def news_detail(request, id):
    new = news.objects.get(id=id)
    # 浏览量 +1
    new.views += 1
    new.save(update_fields=['views'])
    new = news.objects.get(id=id)

    # 取出评论
    comments = Comment.objects.filter(new=id)

    # 需要传递给模板的对象
    context = {'new': new, 'comments': comments, }
    # 载入模板，并返回context对象
    return render(request, 'news/detail.html', context)

def news_search(request):

    data=request.POST['search_text']
    redian = news.objects.order_by('-views')[:4]
    zuixin = news.objects.order_by('-created_time')[:4]
    pinglun = Comment.objects.order_by('-created')[:4]
    tuijian = news.objects.order_by('tui')[:4]
    theme = news.objects.filter(title__contains=data)
    paginator = Paginator(theme, 2) 
     
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:

        contacts = paginator.page(paginator.num_pages)
    

    # context={'redian' :redian,
    #     'zuixin' :zuixin,
    #     'pinglun' :pinglun,
    #     'tuijian' :tuijian,
    #     'contacts' :theme}
    return render(request, 'news/show.html', {'redian' :redian,
        'zuixin' :zuixin,
        'pinglun' :pinglun,
        'tuijian' :tuijian,
        'contacts' :contacts})



def news_show(request, class_name):
    try:
        redian = news.objects.order_by('-views')[:4]
        zuixin = news.objects.order_by('-created_time')[:4]
        pinglun = Comment.objects.order_by('-created')[:4]
        tuijian = news.objects.order_by('tui')[:4]
        class_name = news.objects.filter(category__name=class_name)
        paginator = Paginator(class_name, 2) 
     
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:

            contacts = paginator.page(paginator.num_pages)
    
        return render(request, 'news/show.html', {'redian' :redian,
        'zuixin' :zuixin,
        'pinglun' :pinglun,
        'tuijian' :tuijian,
        'contacts' :contacts})
    except:
        return HttpResponse("news_show没有找到数据！!")


def news_show_tags(request,tags):
    try:
        redian = news.objects.order_by('-views')[:4]
        zuixin = news.objects.order_by('-created_time')[:4]
        pinglun = Comment.objects.order_by('-created')[:4]
        tuijian = news.objects.order_by('tui')[:4]
        class_name = news.objects.filter(tags__name=tags)

        paginator = Paginator(class_name, 2) 

     
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:

            contacts = paginator.page(paginator.num_pages)

        return render(request, 'news/show.html', {'contacts' :contacts,
        'redian' :redian,
        'zuixin' :zuixin,
        'pinglun' :pinglun,
        'tuijian' :tuijian})
    except:
        return HttpResponse("news_show_tags没有找到数据！!")

