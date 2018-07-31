#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这是一个使用Selenium的案例
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    browser = webdriver.Chrome()
    try:
        browser.get('https://www.baidu.com')
        input = browser.find_element_by_id('kw')
        input.send_keys('Python')
        input.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_all_elements_located(
            (By.ID, 'content_left')))
        print('current_url——————————————————')
        print(browser.current_url)
        print('cookies-----------')
        print(browser.get_cookies())
        print('page_source-----------')
        print(browser.page_source)
    finally:
        browser.close()
