#coding=utf-8

from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('wangzi')
print 'OK'