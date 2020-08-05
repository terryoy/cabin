# 临时项目笔记

## 恢复内容

1. main.py
应该是从Lofter的数据包里导出文件到output/archive目录下了。

现在主要的问题是原来在网易博客里面的数据，迁移到LOFTER以后，更新时间都变成了2018年的时间。如果要修正这些时间，必须要从terryoy.blog.163.com上面取。


2. bundle.py
这个job是把wordpress里面的内容导出成jekyll格式的markdown，同时把main里面导出到output/archive(复制到output/markdown目录了)的文件也转换一遍，保存到output/jekyll下面


## TODO

1. 从163博客上读取博客内容并修正时间信息到archive里面。
2. 把图片资源下载下来
3. 把新浪博客的内容下载下来
