#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这个逻辑主要演示了requests中的cookies是如何使用的
'''

import requests

if __name__ == '__main__':
    res = requests.get('https://www.baidu.com')
    print(res.cookies)
    for key, value in res.cookies.items():
        print('key: ' + key + ', value: ' + value)
