#!/usr/bin/env python
# coding=utf-8
# Finame: demo.py
import urllib2
html = "http://www.baidu.com"
response = urllib2.urlopen(html)
print response.read()
