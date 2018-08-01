#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
import time

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('https://www.taobao.com')
    input = browser.find_element_by_id('q')
    input.send_keys('iPhone')
    time.sleep(1)
    input.clear()
    input.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()
    browser.close()
