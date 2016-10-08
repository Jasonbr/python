#!/usr/bin/env python
# coding=utf-8
# Finame: demo.py
import urllib2
html = "http://www.baidu.com"
request = urllib2.Request(html)
response = urllib2.urlopen(request)
print response.read()
