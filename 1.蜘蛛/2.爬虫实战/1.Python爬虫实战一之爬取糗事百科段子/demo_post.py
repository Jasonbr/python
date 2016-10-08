#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2

values = {"username":"songxi_bo@163.com","password":"songxibo"}
data = urllib.urlencode(values)
user_agent= 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
referer = 'http://www.csdn.net/'
headers = { 'User-Agent': user_agent,'Referer': referer }
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()
