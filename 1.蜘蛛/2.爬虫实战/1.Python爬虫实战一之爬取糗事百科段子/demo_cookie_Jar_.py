#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import cookie

fileaname = 'cookie.txt'
# 声明一个MozillaCookieJar来对象实例来保存cookie，之后的写 文档
cookie = cookielib.MolzillaJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlopen({
    'stuid': '201200131012',
    'pwd':'23342321'
    })
# 登陆教务系统的url
loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'

# 模拟登陆，并把cookie保存到变量
result = open(loginUrl,postdata)

# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
#利用cookie请求访问一个网址，此网址是成绩查询网址
gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
#请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
