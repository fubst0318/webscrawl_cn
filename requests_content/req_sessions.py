#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
sessions目前的理解，主要是利用这个来实现模拟同一个会话打开
而非打开2个会话，导致cookies不能共用
'''

import requests

if __name__ == '__main__':
    ses = requests.session()
    ses.get('http://httpbin.org/cookies/set/numbers/123456789')
    res = ses.get('http://httpbin.org/cookies')
    print(res.text)
