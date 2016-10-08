#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
values = {}
values['username'] = "songxi_bo@163.com"
values["password"] = "songxibo"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
