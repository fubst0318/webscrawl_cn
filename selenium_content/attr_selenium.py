#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
演示如何获取节点属性
使用get_attribute()方法来获取节点的属性
'''

from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        url = 'https://www.zhihu.com/explore'
        browser.get(url)
        logo = browser.find_element_by_id('zh-top-link-logo')
        print(logo)
        print(logo.get_attribute('class'))
        print('-----------------')
        print(logo.get_attribute('data-za-c'))
    finally:
        browser.close()
