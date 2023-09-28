from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# Create your models here.


# 新闻分类
class Category(models.Model):
    name = models.CharField(verbose_name='新闻分类', max_length=100)
    index = models.IntegerField(default=1, verbose_name='分类排序')

    class Meta:
        verbose_name = '类别管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 新闻标签
class Tag(models.Model):
    name = models.CharField('新闻标签', max_length=100)

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)


    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 新闻
class news(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)

    # 使用外键关联分类表与分类是一对多关系
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    # 使用外键关联标签表与标签是多对多关系
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='封面图片', blank=True, null=True)
    content = RichTextUploadingField(verbose_name='正文')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True, null=True)
    views = models.PositiveIntegerField('阅读量', default=0)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '文章详情'
        verbose_name_plural = '文章管理'

    def __str__(self):
        return self.title

    # 获取文章地址
    def get_absolute_url(self):
        return reverse('news:news_detail', args=[self.id])






# 友情链接
class Link(models.Model):
    name = models.CharField('链接名称', max_length=20)
    linkurl = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'