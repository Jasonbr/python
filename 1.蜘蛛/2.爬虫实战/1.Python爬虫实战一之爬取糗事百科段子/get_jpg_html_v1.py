#!/usr/bin/env python
# coding=utf-8
import os
import urllib
import httplib2
import webbrowser as web

#爬取在线网站

url = "http://www.baidu.com/"
content = urllib.urlopen(url).read()
open("baidu.html","w").write(content)
# 浏览求打开网站
web.open_new_tab("baidu.html")

# 下载图片 审查元素
pic_url = "https://www.baidu.com/img/bd_logo1.png"
pic_name = os.path.basename(pic_url)
urllib.urlretrieve(pic_url,pic_name)

# 本地文件
#content = urllib.urlopen("first.html").read()
#print content

# 下载图片 审查元素
#pic_url = "imgs/bga1.jpg"
#pic_name = os.path.basename(pic_url)
#urllib.urlretrieve(pic_url,pic_name)
