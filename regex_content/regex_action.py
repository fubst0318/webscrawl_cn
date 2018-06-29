#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这个程序主要实现的是对猫眼电影数据电影排名前100的数据抓取，
对应的网站地址是:http://maoyan.com/board/4?offset=0(这个是第一页)
后面的自动按10递增，一直到90。
主要抓取的数据项是：猫眼电影 TOP100 榜的电影名称、时间、评分、图片等信息
'''

import re
import requests
import json
import time
from requests.exceptions import RequestException


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


def parse_page(html):
    results = re.findall(
        r'<i.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?class="name"><a.*?>(.*?)</a>.*?star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?class="integer">(.*?)</i>.*?class="fraction">(.*?)</i></p>', html, re.S)
    for result in results:
        yield{
            'index': result[0],
            'image': result[1],
            'title': result[2].strip(),
            'actor': result[3].strip()[3:] if len(result[3]) > 3 else '',
            'time': result[4].strip()[5:] if len(result[4]) > 5 else '',
            'score': result[5].strip() + result[6].strip()
        }


def write_to_json(content):
    with open('results.txt', 'a', encoding='utf-8') as f:
        print(json.dumps(content))
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def get_page_Info(url):
    try:
        res = requests.get(url, headers=headers)
        if res.status_code == 200:
            return res.text
        return None
    except RequestException:
        return None


if __name__ == '__main__':
    for i in range(0, 10):
        url = 'http://maoyan.com/board/4?offset=' + str(i * 10)
        html = get_page_Info(url)
        for item in parse_page(html):
            print(item)
            write_to_json(item)
