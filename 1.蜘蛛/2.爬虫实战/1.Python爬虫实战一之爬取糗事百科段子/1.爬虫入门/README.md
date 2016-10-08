python爬虫入门之一综述

版本：python2.7

知识概要：
1、python的基础知识学习
2、python中urllib和urllib2库的用法
3、python的正则表达式
4、python的爬虫框架Scrapy
5、python爬虫更高级的功能

爬虫框架的官网文档：http://doc.scrapy.org/en/latest/

1、分析扒网页的方法：urlopen(url,data,timeout)
import urllib2
html = http://www.baidu.com
response = urllib2.urlopen(html)
print response .read()
2、构造Request
request = urllib2.Request(html)
response = urllib2.urlopen(request)
3、post和get数据的传送

post:

values = {}
values['username'] = "songxi_bo@163.com"
values['password'] = "songxibo"
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

get:
import urllib
import urllib2

values = {}
values['username'] = "songxi_bo@163.com"
values['password'] = "songxibo"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

设置Headers
import urllib
import urllib2
url= 'http://www.server.com/login'
user_agent = {'username': 'cqc', 'password': 'xxxx'}
headers = {'User-Agent' :user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

反盗链：
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)','Referer': 'http://www.csdn.net/' }

Proxy(代理)的设置：
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
 urllib2.install_opener(opener)

 timeout设置：
 import urllib2
 response = urllib2.urlopen('http://www.baidu.com',data,10)

http的put和delete方法：
import urllib2
request = urllib2.Request(url,data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)

Debuglog调试：
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

URLError:

import urllib2
try:
    urllib2.urlopen(request)
except urllib2.URLError, e:
    print e.reason


# 获取Cookie保存到变量：
import urllib2
import cookielib

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie
        print 'Name = '+item.name
        print 'Value = '+item.value
1
# re.match(pattern,string[,flags])
这个方法将会从string(我们要匹配的字符串)的开头开始，尝试匹配pattern，一直向后匹配，如果遇到无法匹配的字符，立即返回None，如果匹配未结束已经到达string的末尾，也会返回None。另个结果均表示匹配失败，否则匹配Pattern成功，同时匹配终止，不在对string向后匹配。

# re.search(pattern,string[,flags])
search方法与match方法及其类似，区别在于match()在于match()函数只检测re是不是在string的开始位置匹配，search()会扫描正个string查找匹配，match()只有在0位置匹配成功的话才有返回
，如果不是开始位置匹配成功的话，match()就返回None。同样，search方法的返回对象同样match()返回对象方法和属性。

# re.split(pattern, string[,maxsplit])
按照能匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割，我们通过下面的列子感受一下。

# re.findall(pattern,string[,flags])
搜索string,以列表形式返回全部能匹配的子串。

refinditer(pattern,string[,flags])
搜索string，返回一个顺序访问每个匹配结果的迭代器。

re.sub(pattern,repl,string[,count])
使用repl替换string中每一个匹配的子串后返回替换的字符串。
当repl是一个字符串时，可以适用\id或\g、\g引用分组，但不能使用编号0.
当repl是一个方法时，这个方法应当只接收一个参数（match对象），并返回一个字符串用于替换
（返回的字符串中不能再引用分组）
count用于指定最多替换次数，不指定时全部替换。

re.subn(pattern,repl,string[,count])

函数API列表：
search(string[, pos[, endpos]]) | re.search(pattern, string[, flags])
split(string[, maxsplit]) | re.split(pattern, string[, maxsplit])
findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])
finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags])
sub(repl, string[, count]) | re.sub(pattern, repl, string[, count])
subn(repl, string[, count]) |re.sub(pattern, repl, string[, count])
