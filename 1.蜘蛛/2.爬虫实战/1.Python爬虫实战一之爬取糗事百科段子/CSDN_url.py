#!/usr/bin/env python
# coding=utf-8
import re
import urllib

url = "http://www.csdn.net/"
content = urllib.urlopen(url).read()
urls = re.findall(r"<a.*?href=.*?<\/a>",content, re.I)
for url in urls:
    print unicode(url,'utf-8')
link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')",content)
for url in link_list:
    print url

