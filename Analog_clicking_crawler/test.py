# -*- coding: utf8 -*-
from selenium import webdriver
from time import clock
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
start=clock()
driver.get(url)#需要测试响应时间的url地址
finish=clock()
print (finish-start)