#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/11 15:25
# @Author  : YJ@SHOU
# @File    : shanghaiwater
# @Software: PyCharm


import sys
from bs4 import BeautifulSoup
import re
import urllib.parse
import urllib.request
import requests
import importlib

importlib.reload(sys)

pageurl = 'http://bmxx.shanghaiwater.gov.cn/shsw/KSDW.asp'
page = urllib.request.urlopen(pageurl)
htmlpage = page.read()
soup = BeautifulSoup(htmlpage,'html.parser')

strsoup=str(soup)
res_tr = r'<table align="center" border="0" cellpadding="0" cellspacing="2" width="100%">(.*?)</table>'
m_tr = re.findall(res_tr,strsoup,re.S|re.M)
for line in m_tr:
    #print (line)
    res = r'<tr height="20">(.*?)</tr>'
    rename = re.findall(res,line,re.S|re.M)
    for name in rename:
        #print (name)
        tname = r'<td class="KSDW_JZ" (.*?)>(.*?)</td>'
        retname = re.findall(tname,name,re.S|re.M)
        print (retname)
        for rname in retname:
            #print (rname[1])
            print (rname[1])


            enurlname = urllib.request.quote(rname[1])
            url = "http://bmxx.shanghaiwater.gov.cn/shsw/proxy/proxy.ashx?http://31.16.1.101/ArcGIS/rest/services/shsw_QUYUFANWEI/MapServer/24/query?f=json&where=NAME%20=%27"+enurlname+"%27&returnGeometry=true&spatialRel=esriSpatialRelIntersects&callback=dojo.io.script.jsonp_dojoIoScript9._jsonpCallback"

            wp = urllib.request.urlopen(url)
            content = wp.read()
            fp = open("d:\\Projects\\waterdata\\"+rname[1]+".html","wb")
            fout = open("d:\\Projects\\waterdata\\"+rname[1]+".html",'w')
            fout.write("<meta charset=\"utf-8\">")
            fp.write(content)

            fp.close()