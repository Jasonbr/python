#!/usr/bin/env python
# coding=utf-8

import urllib2
import cookielib
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()

#从文件中读取cookie内容到变量
cookie.load('cookie.txt',ignore_discard=True, ignore_expires=True)

# 创建请求的request
req = urllib2.Request("http://www.baidu.com")

#利用Urllib2的build_opener方法创建一个Opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()
