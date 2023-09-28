from django.contrib import admin
from .models import news, Link,Category, Tag, Tui
# Register your models here.


@admin.register(news)
class NewsAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ('id','category','img','title','excerpt', 'user',
                    'tui','views','created_time','modified_time')

    # list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 5
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-created_time',)
    # list_editable 设置默认可编辑字段，在列表里就可以编辑
    list_editable = ['title', 'user']
    # fk_fields 设置显示外键字段
    fk_fields = ['category']



# @admin.register(Link)
# class LinkAdmin(admin.ModelAdmin):
#     # 展示字段
#     list_display = ('id', 'name', 'linkurl')
#     # search_fields 设置搜索字段
#     search_fields = ['id', 'name']
#     list_per_page = 10

# @admin.register(Tui)
# class LinkAdmin(admin.ModelAdmin):
#     # 展示字段
#     list_display = ('id', 'title')
#     # search_fields 设置搜索字段
#     search_fields = ['id', 'title']
#     list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ('id', 'name', 'index')
    # search_fields 设置搜索字段
    search_fields = [ 'id', 'name']
    list_per_page = 10


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ('id', 'name',)
    # search_fields 设置搜索字段
    search_fields = ['id', 'name']
    list_per_page = 10


admin.site.site_header = '新闻发布管理后台'
admin.site.site_title = '新闻发布管理系统'