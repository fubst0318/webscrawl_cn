#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver import ActionChains
import time

if __name__ == '__main__':
    browser = webdriver.Chrome()
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    time.sleep(5)
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
