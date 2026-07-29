---
layout: post
title: "学习笔记Swing设计实例——SqlJetBrowser"
date: 2011-05-11 00:00:00
tags: [旧博客存档, 新浪博客]
categories: 
---

id="sina_keyword_ad_area2" class="articalContent   ">

本文是观察SqlJet的DBBrowser以剖析Swing应用的设计方法。

一、Main程序DBBrowser:

DBBrowser类通过main()函数启动这个Swing程序，其中用到SwingUtilities.invokeLater(new

Runnable(){run(){}})的方式来写起始代码。

run()里面所做的事情：

1.新建一个JFrame，并添加了addWindowListerner(new

WindowAdapter())：定义了windowClosing(Event e)的行为。

2.getContentPane().setLayout(new

BorderLayout())：定义一个LayoutManager。

3.setContentPane()：定义了一个BrowserComponentManager。manager.create(frame)，manager.open(null)

4.setJMenuBar：初始化了一个Menu，作为窗口的MainMenu。createMainMenu(BrowserComponentManager).

这个BrowserComponentManager是sqljet.browser包里面用于管理菜单项的Actions的，包括有AboutAction，CloseAction，OpenAction，ExitAction。。等。

二、DBBrowserConfig配置程序

有LatestDirectory, RecentDBs,

WindowSize三个东西的配置，都是通过java.util.Preferences来记录的。Preferences的好处是可以将个性化设置项记录在系统的某个位置，例如文件，系统注册表，目录服务或SQL数据库，而使用这个类的设计者不需要考虑它真正是记录在哪里的。为了使各个设计者使用的配置项不冲突，Preferences通过”userNodeForPackage(class)的方法来设定在哪个node下放这些配置项。它可以用来放布尔，数值，以及字符串等基本类型。

 

三、BrowserComponentManager组件管理器

这个管理器是真正管理着整个窗体所有组件的类，初始化参数是一个JFrame对象（作为它的Owner）。

1.BrowserComponentManager的主要成员变量：

JPanel和JTabbedPane -

JPanel是作为这个Manager本身所代表的一个基础对象。TabbedPane则是本身所需要的一个tab形式的界面元素。

IBrowserComponent -

这是SqlJetBrowser定义的一个接口，可通过getComponent()返回一个JComponent对象。每一个IBrowserComponent对应了窗体里一个tab

page，有mySchemaPage和myDataPage。

Set<IBrowserComponent> -

变量名myInactivatedPages，用于放置前面所说的tab pages。

ExecuterService -

用于执行action的执行服务，是java.util.concurrent里面设计的，初始化方法是Executers.newSingleThreadExecutor()

Collection<Future<?>>

- myScheduledTasks，其实就是一个任务队列。

JProgressBar - 一个通用的进度条

Set<ChangeListener> -

当然就是manager本身的一个listener集合啦，用来发送ChangeEvent的。

2.BrowserComponentManager的主要方法：

BrowserComponentManager create(JFrame owner) -

类似getInstance()

void add/removeChangeListener(ChangeListener listener)

-

添加删除ChangeListener。ChangeListerner和ChangeEvent都是java.swing.event

void fireStateChange() -

对ChangeListener队列里面的listener发送一个本对象的ChangeEvent。

JComponent  getComponent() -

其实是一个初始化myPanel的过程，如果myPanel已经初始化了，则直接返回myPanel。初始化的过程中要做的有：初始化前面所说的对象实例，将IBrowserComponent组合到Panel里面，初始化Listener，将该可视化的可视化，不该可视化的隐藏。这里面有一个putCientProperty的方法，用意应该是将UI

component的控制对象做一个引用，在后面该component被触发时，可以找引用的这个控制对象执行相应的action。

void schedule(final IBrowserRunnable runnable, boolean

cancelAll) - 用于启动task的方法，将runnable提交到myExecuter里面。

void start(final String name, final int total)/void

current(final int current)/void finish() -

用于控制progressbar的三个函数, 是继承IProgress接口的方法。

void stateChanged(ChangeEvent e)/void getActivePage() -

激活change

event所对应的IBrowserComponent对象，从myInactivatedPages里面去掉这一个对象，并执行该对象的初始化工作（open(dbFile))。stateChanged()是继承自ChangeListener接口的方法。

showErrorDialog(Throwable th) -

用来做弹出信息显示框的一个方法。使用的是JDialog对象，里面会包含JPanel, JLabel,

JTextarea，以及两个button“close”和“copy”。注意dialog会setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)

由此看出，BrowserComponentManager这个类是用来做一个全局性控制的框架类，会将主窗口布局的基本UI统筹在一起，并初始化负责每个模块的view(page)。还有就是处理消息的机制，以及执行多线程任务的机制。

分享：

喜欢

<!--

0

赠金笔

-->

0

赠金笔

阅读┊

收藏

┊

喜欢▼

┊打印┊举报/Report

<!--

已投稿到：

排行榜

-->

加载中，请稍候......

后一篇：Persona人物角色中Goals的设定

var voteid="";

  

新浪BLOG意见反馈留言板　欢迎批评指正

新浪简介 | About Sina | 广告服务 | 联系我们 | 招聘信息 | 网站律师 | SINA English | 产品答疑

Copyright © 1996 - 2022 SINA Corporation,  All Rights Reserved

新浪公司 版权所有

var scope = {

$newTray : 1,

$setDomain : true,

$uid : "1651898032",

$PRODUCT_NAME : "blog7",      //blog7photo,blog7icp

$pageid : "article",

$key :  "c12250ac3b201f16a85931d8b50f3405",

$uhost : "",

$ownerWTtype :"",

$private: {"pageset":2,"tj":0,"adver":0,"sms":0,"ad":0,"blogsize":0,"cms":0,"hidecms":1,"top":0,"invitationset":0,"p4p":0,"spamcms":2,"init7":1,"quote":0,"foot":0,"isprivate":0,"headpic":1,"t_sina":"1651898032","oauth_token":"1","oauth_token_secret":"1","uname":"","p_push_t":0,"p_get_t":1,"medal7":3,"articleclass":"117","unbind":""},

$summary: "本文是观察SqlJet的DBBrowser以剖析Swing应用的设计方法。 一、Main程序DBBrowser:  DBBrowser类通过main()函数启动这个Swing程序，其中用到Swin...  (来自 @头条博客)",

$is_photo_vip:0,

$nClass:0,

$articleid:"6275f6b00100rjnb",

$sort_id:117,

$cate_id:"",

$isCommentAllow:1,

$album_pic:"",

$pn_x_rank:1024,

$x_quote_c:"",

$flag2008:"",

component_lists:{"2":{"size":730,"list":[920]},"1":{"size":210,"list":[901]}},

formatInfo:1,

UserPic:[{"pid":null,"repeat":null,"align-h":null,"align-v":null,"apply":null},{"pid":null,"repeat":null,"align-h":null,"align-v":null,"apply":null},{"pid":null,"repeat":null,"align-h":null,"align-v":null,"apply":null}],

UserBabyPic:{"photoX":0,"photoY":0,"photoURL":null,"angle":0,"zoom":0,"maskX":0,"maskY":0,"maskURL":null,"frameURL":null},

UserColor:"",

backgroundcolor:"",

$shareData:{"title":"\u5b66\u4e60\u7b14\u8bb0Swing\u8bbe\u8ba1\u5b9e\u4f8b\u2014\u2014SqlJetBrowser@\u65b0\u6d6a\u535a\u5ba2","content":"\u672c\u6587\u662f\u89c2\u5bdfSqlJet\u7684DBBrowser\u4ee5\u5256\u6790Swing\u5e94\u7528\u7684\u8bbe\u8ba1\u65b9\u6cd5\u3002 \u4e00\u3001Main\u7a0b\u5e8fDBBrowser:  DBBrowser\u7c7b\u901a\u8fc7main()\u51fd\u6570\u542f\u52a8\u8fd9\u4e2aSwing\u7a0b\u5e8f\uff0c\u5176\u4e2d\u7528\u5230SwingUtilitie...  (\u6765\u81ea @\u5934\u6761\u535a\u5ba2)","url":"\/\/blog.sina.com.cn\/s\/blog_6275f6b00100rjnb.html","pic":""},

tpl:"30_1",

reclist:0

};

var $encrypt_code = "58ec29d47e96a966f5e09412b38cda41";

__load_js();

__render_page();

<!--

bShare.addEntry({pic: "", title:"分享自terryoy  《学习笔记Swing设计实例——SqlJetBrowser》", summary:"本文是观察SqlJet的DBBrowser以剖析Swing应用的设计方法。 一、Main程序DBBrowser:  DBBrowser类通过main()函数启动这个Swing程序，其中用到Swin...  (来自 @头条博客)"});

-->

var slotArr = ['atcTitLi_SLOT_41', 'atcTitLi_SLOT_42','loginBarActivity']; //广告位id

var sourceArr = ['SLOT_41','SLOT_42','SLOT_43,SLOT_47,SLOT_48'];  //广告资源id

SinaBlog680.staticBox(slotArr, sourceArr);
