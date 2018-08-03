#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里是演示如何获取iframe的相关信息
主要关注的方法是:switch_to.frame()
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
        browser.get(url)
        browser.switch_to.frame('iframeResult')
        try:
            logo = browser.find_element_by_class_name('logo')
        except NoSuchElementException:
            print('NO LOGO')
        browser.switch_to.parent_frame()
        logo = browser.find_element_by_class_name('logo')
        print(logo)
        print(logo.text)
    finally:
        browser.close()
