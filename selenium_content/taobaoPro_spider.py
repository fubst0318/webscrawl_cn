#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
这里面主要演示的是如何获取淘宝搜索100页的'iPad'商品的各项信息
主要信息包括：商品图片、名称、价格、购买人数、店铺名称、店铺所在地
初始入口链接: https://s.taobao.com/search?q=iPad
主要使用的工具包括: Selenium\PyQuery\MongoDB
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as py
from urllib.parse import quote
from pymongo import MongoClient
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'
client = MongoClient(host='localhost', port=27017)
db = client['taobao']
collection = db.taobao
MAX_PAGE = 100


def index_page(page):
    """
    抓取索引页
    :param page:页码
    通过页面点击事件跳转到相应的画面，并保证需要获取的商品信息已加载完毕
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    """
    提取商品数据,具体项目如下：
    商品图片、名称、价格、购买人数、店铺名称、店铺所在地
    """
    html = browser.page_source
    doc = py(html)
    items = doc('.m-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    """
    保存至 MongoDB
    :param result:结果
    """
    try:
        if collection['products'].insert(result):
            print('存储到MongoDB成功')
    except Exception:
        print('存储到MongoDB失败')


def main():
    """
    遍历每一页
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)
    browser.close()


if __name__ == '__main__':
    main()
