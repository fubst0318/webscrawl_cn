#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
尝试不停的刷新网址：
https://m.weibo.cn/api/container/getIndex?uid=1638782947&luicode=20000174&type=uid&value=1638782947&containerid=1005051638782947
直到跳出验证码位置
----- 经验证不停的刷新，不用出现验证码
'''

import time
from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        while True:
            browser.get(
                'https://m.weibo.cn/api/container/getIndex?uid=1638782947&luicode=20000174&type=uid&value=1638782947&containerid=1005051638782947')
            time.sleep(2)
    finally:
        browser.close()
