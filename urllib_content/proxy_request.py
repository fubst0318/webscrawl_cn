#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.error import URLError
from urllib.request import build_opener, ProxyHandler

proxyHandler = ProxyHandler({
    'http': 'http://127.0.0.1:9743',
    'https': 'https://127.0.0.1:9743'
})

opener = build_opener(proxyHandler)


if __name__ == '__main__':
    try:
        res = opener.open('https://www.baidu.com')
        print(res.read().decode('utf-8'))
    except URLError as e:
        print(e.reason)
