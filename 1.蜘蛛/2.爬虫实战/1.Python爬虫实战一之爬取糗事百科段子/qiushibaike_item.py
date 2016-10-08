#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import re
page = 4
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
            'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImg = re.rearch("img",item[3])
        if not haveImg:
            print item[0],item[1],item[2],item[4]
#    print response.read()
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
