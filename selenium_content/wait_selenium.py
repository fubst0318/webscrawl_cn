#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这是显式等待的例子
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.taobao.com/')
        wait = WebDriverWait(browser, 10)
        input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.btn-search')))
        print(input, button)
    finally:
        browser.close()
