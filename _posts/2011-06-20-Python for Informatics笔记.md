---
layout: post
title: "Python for Informatics笔记"
date: 2011-06-20 00:00:00
tags: [旧博客存档, 新浪博客]
categories: 
---

id="sina_keyword_ad_area2" class="articalContent   ">

1. Common Tasks

a. Files(os.walk)

i. Basic Usage:

import os

cwd = os.getcwd() # current working directory

os.path.abspath('memo.txt') # get absolute path from a relative

path

os.path.exists('memo.txt') # check existence

os.path.isdir('memo.txt) # check dir or file

os.listdir(cwd) # list dirs and files

os.walk('e:/') # returns a (dirname, dirs, files) tuple

os.path.join(dirname, filename*) # get a path with the dir name

and file name, this avoids slash difference

os.path.getsize(file) # get the file size

fhand = open(file, 'r') # open a file reading handler

fhand.read() # return the string content of the file

for(line in fhand) # read lines

fhand.close() # remember to close the handler while

os.remove(thefile) # delete a file

ii. Example: 1. count the text files in a directory; 2. get the

file size; 3.check the contents of those files with multiple lines;

4. filter those bad files with bad content.

iii. Command line arguments:

name = raw_imput('Enter file')

Import sys

sys.argv # a list of command arguments starting with the file

itself

fp = os.popen("ls -l") # open

a pipe(unix) with a shell command, the return value is a file

pointer that behaves just like an open file; and when you're done,

you close the pipe like a file

iv. Exercise: find duplicate files - use a dictionary where the

key is the file size and the value is the full path name, if you

have a duplicate size file and then print out both file name; you

can use a MD5 checksum to check if the two files are

identical: import hashlib; checksum =

hashlib.md5(data).hexdigest()

 

b. Network(socket) and Web(urllib)

i. socket:

import socket # a socket is like a file, except it's two-way

connection between two programs

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(('www.py4inf.com', 80)) # a tuple that contains

host and port

mysocket.send('GET http://www.py4inf.com/code/romeo.txt

HTTP/1.0\n\n') // send a message by the socket

mysocket.recv(512) # receive a segment within the size of

512

ii. urllib:

import urllib # the difference with socket is it auto proceeds

the HTTP headers

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt'[,

data, proxies]) # proxies and data are dictionaries defined as

{'key':value}

for(line in fhand) # the reading method is not the same as

socket

iii. Parsing(Scraping) HTML(BeautifulSoup - www.crummy.com)

html = urllib.urlopen(url).read

soup = BeautifulSoup(html)

tags = soup('a') # retrieve all of the anchor tags

tag.get('href', none)

tag.attrs

c. Web Services

i. Parsing xml:

import xml.etree.ElementTree a ET # xml tool import

ET.fromstring(data) # convert from string to XML tree

node = tree.find(element_name) # return a node

node.text, node.get(attr) # return text content in the node, and

get attribute of the node

tree.findall('users/user') # return a list of users in

"users"

ii. Web Service API

1. Feed url. (e.g. 'http://api.douban.com/people/{userId}/miniblog')

2. Encoding:

req = urllib.urlopen(url, data, proxies);

encoding = req.headers['content-type'].split('charset=')[-1]

document = req.read()

print unicode(document, encoding)

3. Restful?

d. Database

i. Basic:

import sqlite3

conn = sqlite3.connect('music.db')

cur = conn.cursor() # like a file handler that to perform

operations on the data

cur.execute('DROP TABLE IF EXISTS Tracks') # drop table

cur.execute('CREATE TABLE Tracks(title TEXT, plays INTEGER)') #

create table

cur.execute('INSERT INTO Tracks (title, plays) VALUES(?, ?)',

('My Way', 15)) # insert the records with parameters and a

tuple

conn.commit()

cur.execute('SELECT title, plays FROM Tracks')

for row in cur:

print row # shows "(u'My Way',

15)" tuple

conn.close() # close connection

ii. Spridering Twitter: use sqlite3, urllib,

xml.etree.ElementTree to retrieve friends with names

iii. Data modeling: design the relational models for the

data

CREATE TABLE Pals(from_friend TEXT, to_friend TEXT)

CREATE TABLE People(id INTEGER PRIMARY KEY, name TEXT UNIQUE,

retrieved INTEGER)

CREATE TABLE Follows(from_id INTEGER, to_id INTEGER,

UNIQUE(from_id, to_id))

 

e. Extra(Personally Added)

i. JSON:

import json # import json library

json.loads(jsonstr[, params]) # deserialize a JSON formatted str

to a Python object

json.dumps(obj) # serialize obj to a JSON formatted str

json.load()/write() without 's' converted to a stream with a

.write()/.read() file-like object

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

$summary: "1. Common Tasks a. Files(os.walk) i. Basic Usage: import os cwd = os.getcwd() # current working direct...  (来自 @头条博客)",

$is_photo_vip:0,

$nClass:0,

$articleid:"6275f6b00100t9m5",

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

$shareData:{"title":"Python for Informatics\u7b14\u8bb0@\u65b0\u6d6a\u535a\u5ba2","content":"1. Common Tasks a. Files(os.walk) i. Basic Usage: import os cwd = os.getcwd() # current working directory os.pa...  (\u6765\u81ea @\u5934\u6761\u535a\u5ba2)","url":"\/\/blog.sina.com.cn\/s\/blog_6275f6b00100t9m5.html","pic":""},

tpl:"30_1",

reclist:0

};

var $encrypt_code = "58ec29d47e96a966f5e09412b38cda41";

__load_js();

__render_page();

<!--

bShare.addEntry({pic: "", title:"分享自terryoy  《Python for Informatics笔记》", summary:"1. Common Tasks a. Files(os.walk) i. Basic Usage: import os cwd = os.getcwd() # current working direct...  (来自 @头条博客)"});

-->

var slotArr = ['atcTitLi_SLOT_41', 'atcTitLi_SLOT_42','loginBarActivity']; //广告位id

var sourceArr = ['SLOT_41','SLOT_42','SLOT_43,SLOT_47,SLOT_48'];  //广告资源id

SinaBlog680.staticBox(slotArr, sourceArr);
