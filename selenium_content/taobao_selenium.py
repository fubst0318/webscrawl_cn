#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
演示下如何直接获取淘宝网的所有源码
'''

from selenium import webdriver


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    print(browser.page_source)
    browser.close()
