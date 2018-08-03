#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里演示selenium 执行画面的前进及后退操作
'''

from selenium import webdriver
import time

if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com/')
        browser.get('https://www.taobao.com/')
        browser.get('https://www.python.org/')
        browser.back()
        time.sleep(1)
        browser.forward()
    finally:
        browser.close()
