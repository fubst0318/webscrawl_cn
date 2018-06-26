#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
使用代理，这里是一个样例
'''

import requests

proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

if __name__ == '__main__':
    res = requests.get('https://www.taobao.com', proxies=proxies)
