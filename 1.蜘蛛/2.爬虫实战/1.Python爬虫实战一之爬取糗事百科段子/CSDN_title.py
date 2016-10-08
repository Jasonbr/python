#!/usr/bin/env python
# coding=utf-8
import re
import urllib

url = "http://www.csdn.net/"
content = urllib.urlopen(url).read()

print u'方法一:'
title_pat = r'(?<=<title>).*?(?=</title>)'
title_ex = re.compile(title_pat,re.M|re.S)
title_obj = re.search(title_ex,content)
title = title_obj.group()
print title

print u'方法二:'
title = re.findall(r'<title>(.*?)</title>',content)
print title[0]
