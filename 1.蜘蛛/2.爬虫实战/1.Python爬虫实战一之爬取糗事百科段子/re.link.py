#!/usr/bin/env python
# coding=utf-8
import re

content = '''
<td>
<a href="https://www.baidu.com/articles/zj.html" title="浙江省">浙江省主题介绍</a>
<a href="https://www.baidu.com//articles/gz.html" title="贵州省">贵州省主题介绍</a>
</td>
'''
# 获取<a href></a>之间的内容
print u'获取链接文本内容:'
res = r'<a .*?>(.*?)</a>'
mm = re.findall(res,content,re.S|re.M)
for value in mm:
    print value

# 获取所有<a href></a>链接所有的内容
print u'\n获取完整链接的内容:'
urls = re.findall(r"<a.*?href=.*?<\/a>",content,re.I|re.S|re.M)
for i in urls:
    print i
# 获取<a href></a>中的URL
print u'\n获取链接中URL:'
res_url = r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')"
link = re.findall(res_url, content, re.I|re.S|re.M)
for url in link:
    print url
