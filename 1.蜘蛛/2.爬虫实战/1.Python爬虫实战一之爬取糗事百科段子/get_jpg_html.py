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
