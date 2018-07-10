#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里演示怎么获取马云微博信息
相关链接是:https://m.weibo.cn/u/2145291155
这里主要演示的是ajax相关爬虫技术
通过chrome 查看上个链接的xhr的相关链接，标准格式为:
https://m.weibo.cn/api/container/getIndex?
type=uid&value=2145291155&containerid=1076032145291155&page=5&standalone=0
主要的参数:type\value\containerid\page
其中，type,value,containerid不变，而且containerid 相当于用户名前面加了107603
      page显示的是当前页面
'''

import requests
from urllib.parse import urlencode
from pymongo import MongoClient
from pyquery import PyQuery as pq

base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2145291155',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
client = MongoClient(host='localhost', port=27017)
db = client['weibo']
collection = db.weibo
max_page = 16


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page': page,
        'standalone': 0
    }
    url = base_url + urlencode(params)
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.json(), page
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json, page: int):
    if json:
        items = json.get('data').get('cards')
        for index, item in enumerate(items):
            if page == 1 and index == 1:
                continue
            else:
                item = item.get('mblog')
                weibo = {}
                weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['attributes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    for page in range(1, max_page + 1):
        json = get_page(page)
        results = parse_page(*json)
        for result in results:
            print(result)
            save_to_mongo(result)
