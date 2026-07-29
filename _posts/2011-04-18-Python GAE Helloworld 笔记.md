---
layout: post
title: "Python GAE Helloworld 笔记"
date: 2011-04-18 00:00:00
tags: [旧博客存档, 新浪博客]
categories: 
---

id="sina_keyword_ad_area2" class="articalContent   ">

Google App Engine的Python教程入门路线：

1. plain text版的request和response

2. 加入MainPage类实现的plain text helloworld

3. 加入user login功能

4. 加入form处理实现的guestbook网页

5. 加入data store(model)的功能，存储guest book数据

6. 将guest book页面改成带user login，网页模板功能

7. 上传GAE空间

 

app.yaml文件配置模板：

application: py-teatime

version: 1

runtime: python

api_version: 1

handlers:

- url: /stylesheets

  static_dir: stylesheets

- url: /.*

  script: helloworld.py

 

开发环境server：

dev_appserver.py py-teatime/

上传应用程序命令：

appcfg.py update helloworld/

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

$summary: "Google App Engine的Python教程入门路线： 1. plain text版的request和response 2. 加入MainPage类实现的plain text helloworld...  (来自 @头条博客)",

$is_photo_vip:0,

$nClass:0,

$articleid:"6275f6b00100qo0q",

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

$shareData:{"title":"Python GAE Helloworld \u7b14\u8bb0@\u65b0\u6d6a\u535a\u5ba2","content":"Google App Engine\u7684Python\u6559\u7a0b\u5165\u95e8\u8def\u7ebf\uff1a 1. plain text\u7248\u7684request\u548cresponse 2. \u52a0\u5165MainPage\u7c7b\u5b9e\u73b0\u7684plain text helloworld 3. \u52a0\u5165use...  (\u6765\u81ea @\u5934\u6761\u535a\u5ba2)","url":"\/\/blog.sina.com.cn\/s\/blog_6275f6b00100qo0q.html","pic":""},

tpl:"30_1",

reclist:0

};

var $encrypt_code = "58ec29d47e96a966f5e09412b38cda41";

__load_js();

__render_page();

<!--

bShare.addEntry({pic: "", title:"分享自terryoy  《Python GAE Helloworld 笔记》", summary:"Google App Engine的Python教程入门路线： 1. plain text版的request和response 2. 加入MainPage类实现的plain text helloworld...  (来自 @头条博客)"});

-->

var slotArr = ['atcTitLi_SLOT_41', 'atcTitLi_SLOT_42','loginBarActivity']; //广告位id

var sourceArr = ['SLOT_41','SLOT_42','SLOT_43,SLOT_47,SLOT_48'];  //广告资源id

SinaBlog680.staticBox(slotArr, sourceArr);
