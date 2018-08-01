#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
使用selenium执行javascript脚本
'''

from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
    browser.close()
