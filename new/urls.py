from django.urls import path 
from django.conf.urls import url
from . import views

# 正在部署的应用的名称
app_name = 'news'

urlpatterns = [
    # path函数将url映射到视图
    path('', views.new_list, name='new_list'),
    # 文章详情
    path('news-detail/<int:id>/', views.news_detail, name='news_detail'),
    url(r'^search/$', views.news_search ),
    # path('search/<str:theme>/', views.news_search, name='news_search'),

    path('daohang/<str:class_name>/', views.news_show, name='news_show'),

    path('daohang/<str:tags>/', views.news_show_tags, name='news_show_tags')
]