#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这个主要是实现对今日头条 ‘街拍’内容的抓取
参考的一个xhr链接为：
https://www.toutiao.com/search_content/?offset=20&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab
其中，E:\\toutiao_spy\\ 为个人本地目录
'''

from urllib.parse import urlencode
import requests
import os
from hashlib import md5
from multiprocessing import Pool

GROUP_START = 1
GROUP_END = 5


def get_page(offset):
    params = {
        'offset': offset,
        'keyword': '街拍',
        'format': 'json',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_ta'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            image_list = item.get('image_list')
            title = item.get('title')
            if image_list:
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


def save_image(item):
    if not os.path.exists('E:\\toutiao_spy\\' + item.get('title')):
        os.mkdir('E:\\toutiao_spy\\' + item.get('title'))
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list', 'large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'),
                                             md5(response.content).hexdigest(), 'jpg')
            print(file_path)
            if not os.path.exists('E:\\toutiao_spy\\' + file_path):
                with open('E:\\toutiao_spy\\' + file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
