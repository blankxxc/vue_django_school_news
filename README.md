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
 




 

