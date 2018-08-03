#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里使用隐式等待来等待DOM的响应
可以直接使用 browser.implicitly_wait()
'''

from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    url = 'https://www.zhihu.com/explore'
    try:
        browser.implicitly_wait(10)
        browser.get(url)
        input = browser.find_element_by_class_name('zu-top-add-question')
        print(input)
    finally:
        browser.close()
