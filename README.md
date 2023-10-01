# vue_django_school_news
用django和vue框架实现的校园新闻网站，欢迎star和fork！
# 如何实现
先clone代码
在用power shell进入到存放manage.py文件夹 
输入python manage.py runserver，启动命令

![image](https://github.com/blankxxc/vue_django_school_news/assets/54624981/3e0d54ed-5d13-494e-8837-be5e8e7776df)

服务器开启后，再打开IE7.0（或以上版本）浏览器，在其地址栏中输入：http://127.0.0.1:8000/
（其中localhost为本地主机IP地址，8080为Tomcat服务器端口号）按回车即可进入新闻网首页登录界面。如图所示：

 ![image](https://github.com/blankxxc/vue_django_school_news/assets/54624981/9b61098a-5c4a-4cf1-a655-e28ac618e90e)

 # 功能展示
 作为一个新闻网站，它应该具有新闻网站所有的一些基本功能，包括：用户登陆功能，用户浏览新闻的功能以及用户发表评论的功能和管理员添加修改删除新闻的功能等。接下来，我将详细阐述一下这些功能。
（一）、用户登录功能
进入登录页面后，对于第一次登陆的用户来说，首先需要注册，单击“注册账号”按钮即可进入注册界面,注册完成后返回登录界面。然后，在对应的地方分别输入用户名和密码，点击“提交”按钮，系统即将用户名和密码发送到网络服务器上，与保存在服务器数据库中的信息进行核对。若核对正确，则进入帖子浏览的界面，若不正确，则重新返回登录界面。


（二）、用户注册功能
 进入到注册界面，输入昵称，邮箱，设置密码和再次确认密码，点击“提交”按钮，将表单数据发送到后台进行过滤确认之后，存储到数据库当中。

（三）、用户新闻的浏览

1、新闻网首页
首页顶部是导航栏可以设置了相对路径，会根据滑动而发生移动。顶部导航栏有侧面导航栏的展开按钮，首页的跳转，搜索以及回到顶部。
 

首页上半部分有着一些展示信息如可以切换的公告，轮播图，还有广告位置。
 

首页的下半部分的左侧是各个类别的新闻的前几个进行展示，第一个会有图片有摘要等等，详细介绍。

首页下半部分是三格栏，可以进行热点新闻、最新新闻、最新评论的网页进行切换展示。还有推荐新闻可以浏览，最后是一些个人信息介绍。

 

网页底部就是一些信息，跳转界面还没有完善。


2、查看列表新闻
点击侧边导航栏跳转到各个类别的新闻的详细列表内。也可以通过搜索跳转查看新闻列表。

 

3、用户查看详细新闻内容.
新闻内容展示了新闻标题、作业、发布时间、浏览量以及详细内容。文章最后还有评论窗口可以进行评论，输入到评论窗口，点击发送，就可以评论文章了，可以出现评论的时间，评论的内容，未登录是不可以评论的。

 

（四）、管理员对新闻的查看/发表/删除/修改/查找功能

1、管理员界面登录输入账号密码
      

2、管理员首页可以全屏，切换各类主题，跳转到各个管理、显示之前的操作等等。
 

3、管理员对标签进行排序、查找

4、对新闻的增删改

# 系统文件

文件夹名	文件名	功能
news	setting	设计总体的情况，例如连接的数据库是什么
	urls	路由跳转到各个文件夹下的url
templates	base.html	Html的头文件，写标题以及导入各类js，css样式
	header.html	网页页头的导航栏
	footer.html	网页页尾的书写
	index.html	首页的书写
	detail.html	新闻详情页，写内容
	show.html	列表展示各类新闻
	login.html	登录界面
	register.html	用户注册界面
static	img	放置图片
	js	存放js类文件
	css	存放css类文件
	fonts	存放各类ui的小图标
media	日期类文件夹	放各类上传的图片，用于新闻封面展示
new(用于新闻的各类展示)	admin	用于后台管理系统的设计
	url	路由用于跳转到views的对应函数
	view	用于数据库数据的提取、处理与存放
	models	各类表的创建
comment(用于文章下的评论)	url	用于跳转到相应的views对应函数
	from	用于评论的数据传输
	model	表的建立
uerprofile	url	用于跳转到相应的views对应函数
	from	用于表格数据的过滤、筛选、传输，例如进行密码一致性检验等等
	views	表格数据的处理以及前后端数据传输，以及session数据传输。

# 系统详细设计
（一）、建立数据库及数据库表
建立一个数据库db.sqlite和三个数据库表（Category、Tag、Tui、news、Comment、User）。
首先在SQLite数据库，配置完成后在文件夹下建立名为“db.sqlite”的数据库，然后再建立三个数据库表（Category、Tag、Tui、news、Comment、User）。
创建Category表：
class Category(models.Model):
    name = models.CharField(verbose_name='新闻分类', max_length=100)
    index = models.IntegerField(default=1, verbose_name='分类排序')

    class Meta:
        verbose_name = '类别管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
创建表Tag：
class Tag(models.Model):
    name = models.CharField('新闻标签', max_length=100)

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
创建表Tui：
class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)


    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name;
创建表news：
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

创建Comment表
class Comment(models.Model):
    new = models.ForeignKey(
        news,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.content[:20]
（二）	、用户登录功能的实现
1、登陆界面的制作
（1）判断输入的用户名和密码是否为空：
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

# 注册用户表单
class UserRegisterForm(forms.ModelForm):
    # 复写 User 的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试。")
（2）登陆界面的制作：
<div class="container">
    <div class="row">
        <div class="col-12">
            <br>
            <form method="post">
                {% csrf_token %}
                <!-- 账号 -->
                <div class="form-group">
                    <label for="username">账号</label>
                    <input type="text" class="form-control" id="username" name="username">
                </div>
                <!-- 密码 -->
                <div class="form-group">
                    <label for="password">密码</label>
                    <input type="password" class="form-control" id="password" name="password">
                </div>
                <!-- 提交按钮 -->
                <button type="submit" class="btn btn-primary">提交</button>

            </form>
        </div>
    </div>
</div>


<div class="container">
    <div class="row">
        <div class="col-12">
            <br>
            <br>
            <h5>还没有账号？</h5>
            点击<a href='{% url "userprofile:register" %}'>注册账号</a>加入我们吧！
            <br>
            <form method="post" action=".">

            </form>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
        </div>
    </div>
</div>
2、登陆功能的实现
通过Login.html界面传递参数username 和 password 给from，然后查询数据库，判断用户名和密码是否正确。若判断正确则为用户建立一个session，并进入了用户主界面。
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
        return HttpResponse("请使用GET或POST请求数据")		response.sendRedirect("login.html");
（三）、浏览主题帖子功能的实现
1、翻页功能的实现
功能的实现：首先确定每页所能容纳帖子的最大数目，在这里我设定划分为2；然后连接数据库查询帖子的总数，从而判断总的页数， 
程序为：
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
    
页面的制作：
	<div >
			    <span >
			    	<span >
			        {% if contacts.has_previous %}
			            <a href="?page={{ contacts.previous_page_number }}">&laquo;</a>
			        {% endif %}
			     	</span >
			 		 Page {{ contacts.number }} of {{ contacts.paginator.num_pages }}
			        <span >
			        {% if contacts.has_next %}
			            <a href="?page={{ contacts.next_page_number }}">&raquo;</a>
			        {% endif %}
			        </span>
			    </span>
			</div>
2、浏览新闻的实现
每幅帖子都有三部分组成：标题、封面、时间，通过上述分页功能选出了需要显示出来的帖子，下面就是将它们显示在页面上的程序：
{% for new in contacts %}
        		<br>
        		<br>
				<article class="post-list-small__entry clearfix">
                    <div class="post-list-small__img-holder">
                        <div class="thumb-container thumb-75">
                            <a href="{% url 'news:news_detail' new.id %}">
                                <img data-src="/media/{{new.img}}"
                                     src="/media/{{new.img}}" alt="" class=" lazyload">
                            </a>
                        </div>
                    </div>
                    <div class="post-list-small__body">
                        <h3 class="post-list-small__entry-title">
                            <a href="{% url 'news:news_detail' new.id %}">{{new.title}}</a>
                        </h3>
                        <ul class="entry__meta">
                            <li class="entry__meta-date">
                                <i class="ui-date"></i>
                                {{new.modified_time}}
                            </li>
                        </ul>
                    </div>
                </article>
            {% endfor %}
（四）、新闻内容详细内容页面的制作
通过页面view传递参数ID，然后进行数据库查询获得帖子的详细信息，并显示的页面上。
<div class="container">
    <div class="row">
        <!-- 标题及作者 -->
        <h1 class="col-12 mt-4 mb-4">{{ new.title }}</h1>
        <div class="col-12 alert alert-success">作者：{{ new.user }} &nbsp;&nbsp;&nbsp;&nbsp; 发布时间：{{ new.created_time }}
            &nbsp;&nbsp;&nbsp;&nbsp; 浏览量：{{ new.views }}
        </div>


        <!-- 文章正文 -->
        <div  >
            <p >{{new.content}}</p>
        </div>
    </div>
</div>
（五）、在帖子详细内容页面里实现回复功能
在detail页面里实现评论功能，让用户可以在同一页面实现浏览新闻、评论新闻和浏览别人评论的功能：
1.Detail.html页面中的代码：
此部分代码是显示该帖子的内容，并给用户提供了一个评论按钮，点此按钮可以将框内的评论内容发送到后端：
<div class="container">
    <div class="col-24">
        <form
                action="{% url 'comment:post_comment' new.id %}"
                method="POST"
        >
            {% csrf_token %}

            <div class="form-group">
                <label for="content">
                    <h4>
                        我也要发表评论：
                    </h4>
                </label>
                <textarea
                        type="text"
                        class="form-control"
                        id="content"
                        name="content"
                        rows="2"></textarea> </label>
            </div>
            <!-- 提交按钮 -->
            <button type="submit" class="btn btn-primary ">发送</button>
        </form>
    </div>
    <br>
2.View页面中的代码：
此页面的功能保存由detail.html页面传来的回帖信息，进行筛选判断后再保存信息到Comment数据库表中：
def post_comment(request, id):
    new = get_object_or_404(news, id=id)

    # 处理 POST 请求
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.new = new
            new_comment.user = request.user
            new_comment.save()
            return redirect(new)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 处理错误请求
    else:
        return HttpResponse("发表评论仅接受POST请求。")
（六）、侧边导航栏的设置
   使用bootstrap进行侧边导航栏的书写，并将每个选项都设置一个跳转浏览全部新闻的界面。
	<div class="sidenav__close">
        <button class="sidenav__close-button" id="sidenav__close-button" aria-label="close sidenav">
            <i class="ui-close sidenav__close-icon"></i>
        </button>
    </div>

    <!-- Nav -->
    <nav class="sidenav__menu-container">
        <ul class="sidenav__menu" role="menubar">
            <!-- Categories -->
            <li>
                <a href="{% url 'news:news_show_tags' '学校' %}" class="sidenav__menu-link sidenav__menu-link-category sidenav__menu-link--orange">学校热点</a>
            </li>
            <li>
                <a href="{% url 'news:news_show' '党务工作' %}" class="sidenav__menu-link sidenav__menu-link-category sidenav__menu-link--blue">党务工作</a>
            </li>
            <li>
                <a href="{% url 'news:news_show' '学术交流' %}" class="sidenav__menu-link sidenav__menu-link-category sidenav__menu-link--red">学术交流</a>
            </li>
            <li>
                <a href="{% url 'news:news_show' '各类赛事' %}" class="sidenav__menu-link sidenav__menu-link-category sidenav__menu-link--salad">各类赛事</a>
            </li>
            <li>
                <a href="{% url 'news:news_show' '素质教育' %}" class="sidenav__menu-link sidenav__menu-link-category sidenav__menu-link--purple">素质教育</a>
            </li>
            <li>
                <a href="{% url 'news:news_show' '其他' %}" class="sidenav__menu-link sidenav__menu-link-category sidenav__menu-link--yellow">其他</a>
            </li>
            <li>
                <a href="#" class="sidenav__menu-link">关于</a>
            </li>
        </ul>
（七）、新用户注册功能的实现
	 register.html用于保存新用户的信息，这些信息是由register.html页面传递而来，首先判断用户名是否已被注册过了，若被注册过则提示已注册。
	<div class="container">
    <div class="row">
        <div class="col-12">
            <br>
            <form method="post" action=".">
                {% csrf_token %}
                <!-- 账号 -->
                <div class="form-group col-md-4">
                    <label for="username">昵称</label>
                    <input type="text" class="form-control" id="username" name="username" required>
                </div>
                <!-- 邮箱 -->
                <div class="form-group col-md-4">
                    <label for="email">Email</label>
                    <input type="text" class="form-control" id="email" name="email">
                </div>
                <!-- 密码 -->
                <div class="form-group col-md-4">
                    <label for="password">设置密码</label>
                    <input type="password" class="form-control" id="password" name="password" required>
                </div>
                <!-- 确认密码 -->
                <div class="form-group col-md-4">
                    <label for="password2">确认密码</label>
                    <input type="password" class="form-control" id="password2" name="password2" required>
                </div>
                <!-- 提交按钮 -->
                <button type="submit" class="btn btn-primary">提交</button>
            </form>
        </div>
    </div>
</div>
通过view的函数进行判断是否能够注册，并写入到数据库当中
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
（八）、新闻轮播图
在index.html页面用于封面轮播，用于展示一些新闻热点：

                {% for new in news %}
                <article class="entry featured-posts-grid__entry" >
                    <div class="thumb-bg-holder owl-lazy" data-src="/media/{{ new.img }}" >
                        <img src="/media/{{ new.img }}" alt="" class="d-none" >
                        <a href="{% url 'news:news_detail' new.id %}" class="thumb-url"></a>
                        <div class="bottom-gradient"></div>
                    </div>

                    <div class="thumb-text-holder" >
                        <a href="single-post.html"
                           class="entry__meta-category entry__meta-category-color entry__meta-category-color--salad">
                            {{ new.category }}</a>
                        <h2 class="thumb-entry-title">
                            <a href="{% url 'news:news_detail' new.id %}">{{ new.title }}</a>
                        </h2>
                        <ul class="entry__meta">
                            <li class="entry__meta-author">
                                <i class="ui-author"></i>
                                <a >{{ new.user }}</a>
                            </li>
                            <li class="entry__meta-date">
                                <i class="ui-date"></i>
                                {{ new.modified_time }}
                            </li>
                            <li class="entry__meta-comments">
                                <i class="ui-comments"></i>
                                <a >{{ new.views }}</a>
                            </li>
                        </ul>
                    </div>
                </article>
                {% endfor %}
（九）、三格栏进行新闻展示
	Index.html页面用于三格栅进行展示，获得id并按照浏览量进行排序展示热点，根据时间进行最新区域展示，最近评论进行评论区域展示：
<!-- 三格栅 -->
            <div class="widget widget-tabpost">
                <div class="tabs widget-tabpost__tabs">
                    <ul class="tabs__list widget-tabpost__tabs-list">
                        <li class="tabs__item widget-tabpost__tabs-item tabs__item--active">
                            <a href="#tab-trending" class="tabs__url tabs__trigger widget-tabpost__tabs-url">热点</a>
                        </li>
                        <li class="tabs__item widget-tabpost__tabs-item">
                            <a href="#tab-latest"
                               class="tabs__url tabs__trigger widget-tabpost__tabs-url">最新</a>
                        </li>
                        <li class="tabs__item widget-tabpost__tabs-item">
                            <a href="#tab-comments" class="tabs__url tabs__trigger widget-tabpost__tabs-url">评论</a>
                        </li>
                    </ul> <!-- end tabs -->

                    <!-- tab content -->
                    <div class="tabs__content tabs__content-trigger widget-tabpost__tabs-content">

                        <div class="tabs__content-pane tabs__content-pane--active" id="tab-trending">
                            <ul class="post-list-small">
                                {% for new in redian %}
                                <li class="post-list-small__item">
                                    <article class="post-list-small__entry clearfix">
                                        <div class="post-list-small__img-holder">
                                            <div class="thumb-container thumb-75">
                                                <a href="{% url 'news:news_detail' new.id %}">
                                                    <img data-src="/media/{{new.img}}"
                                                         src="/media/{{new.img}}" alt="" class=" lazyload">
                                                </a>
                                            </div>
                                        </div>
                                        <div class="post-list-small__body">
                                            <h3 class="post-list-small__entry-title">
                                                <a href="{% url 'news:news_detail' new.id %}">{{new.title}}</a>
                                            </h3>
                                            <ul class="entry__meta">
                                                <li class="entry__meta-date">
                                                    <i class="ui-date"></i>
                                                    {{new.modified_time}}
                                                </li>
                                            </ul>
                                        </div>
                                    </article>
                                </li>
                                {% endfor %}
                            </ul>
                        </div>

                        <div class="tabs__content-pane" id="tab-latest">
                            <ul class="post-list-small">
                                {% for new in zuixin %}
                                <li class="post-list-small__item">
                                    <article class="post-list-small__entry clearfix">
                                        <div class="post-list-small__img-holder">
                                            <div class="thumb-container thumb-75">
                                                <a href="{% url 'news:news_detail' new.id %}">
                                                    <img data-src="/media/{{new.img}}"
                                                         src="/media/{{new.img}}" alt="" class=" lazyload">
                                                </a>
                                            </div>
                                        </div>
                                        <div class="post-list-small__body">
                                            <h3 class="post-list-small__entry-title">
                                                <a href="{% url 'news:news_detail' new.id %}">{{new.title}}</a>
                                            </h3>
                                            <ul class="entry__meta">
                                                <li class="entry__meta-date">
                                                    <i class="ui-date"></i>
                                                    {{new.modified_time}}
                                                </li>
                                            </ul>
                                        </div>
                                    </article>
                                </li>
                                {% endfor %}
                            </ul>
                        </div>

                        <div class="tabs__content-pane" id="tab-comments">
                            <ul class="post-list-small">
                                {% for new in pinglun %}
                                <li class="post-list-small__item">
                                    <article class="post-list-small__entry clearfix">
                                        <div class="post-list-small__img-holder">
                                            <div class="thumb-container thumb-75">
                                                <a href="{% url 'news:news_detail' new.new.id %}">
                                                    <img data-src="/media/{{new.new.img}}"
                                                         src="/media/{{new.new.img}}" alt="" class=" lazyload">
                                                </a>
                                            </div>
                                        </div>
                                        <div class="post-list-small__body">
                                            <h3 class="post-list-small__entry-title">
                                                <a href="{% url 'news:news_detail' new.new.id %}">{{new.new.title}}</a>
                                            </h3>
                                            <ul class="entry__meta">
                                                <li class="entry__meta-date">
                                                    <i class="ui-date"></i>
                                                    {{new.new.modified_time}}
                                                </li>
                                            </ul>
                                        </div>
                                    </article>
                                </li>
                                {% endfor %}
                            </ul>
                        </div>

                    </div> <!-- end tab content -->
                </div> <!-- end tabs -->
            </div> <!-- end widget popular/latest posts -->
（十）、搜索功能的使用
输入到表单内进行数据传递。
<div class="nav__right nav--align-right d-lg-flex">
                        <div >
                                <a href="#top" ><i class="ui-arrow-up"></i></a>
                        </div>
                        <!-- Search -->
                        <div class="nav__right-item nav__search">
                            <a href="#" class="nav__search-trigger" id="nav__search-trigger">
                                <i class="ui-search nav__search-trigger-icon"></i>
                            </a>
                            <div class="nav__search-box" id="nav__search-box">
                                <form class="nav__search-form" method="POST" action="/search/">
                                    {% csrf_token %}
                                    <input type="text" placeholder="Search an article" class="nav__search-input" name='search_text' id='search_text'>
                                    <button type="submit" class="search-button btn btn-lg btn-color btn-button">
                                        <i class="ui-search nav__search-icon"></i>
                                    </button>
                                </form>
                            </div>

                        </div>
后续用view的函数进行数据库搜索含有该字的标题的新闻，并用show.html进行展示。
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
（十一）、公告切换功能
	在index.html中调用bootstarp进行轮播图的div展示。
<div class="trending-now">
        <div class="container relative">
            <span class="trending-now__label">公告</span>
            <ul class="newsticker">
                <li class="newsticker__item"><a class="newsticker__item-url">欢迎来到校园新闻首页</a></li>
                <li class="newsticker__item"><a  class="newsticker__item-url">注册登录后方可评论新闻</a></li>
                <li class="newsticker__item"><a  class="newsticker__item-url">发布新闻请联系后台工作人员</a></li>
            </ul>
            <div class="newsticker-buttons">
                <button class="newsticker-button newsticker-button--prev" id="newsticker-button--prev"
                        aria-label="next article"><i class="ui-arrow-left"></i></button>
                <button class="newsticker-button newsticker-button--next" id="newsticker-button--next"
                        aria-label="previous article"><i class="ui-arrow-right"></i></button>
            </div>
        </div>
    </div>



 




 

