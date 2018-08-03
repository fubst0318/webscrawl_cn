#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里演示如何使用selenium操作cookies
'''

from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.zhihu.com/explore')
        print(browser.get_cookies())
        browser.add_cookie(
            {'name': 'name', 'domain': 'www.zhihu.com', 'value': 'tonyxu'})
        print(browser.get_cookies())
        browser.delete_all_cookies()
        print(browser.get_cookies())
    finally:
        browser.close()
