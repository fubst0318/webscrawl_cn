#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import Request, urlopen
from urllib.parse import urlencode

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}

dict = {
    'name': 'TonyXu'
}

data = bytes(urlencode(dict), encoding='utf8')


if __name__ == '__main__':
    req = Request(url, data=data, headers=headers, method='POST')
    res = urlopen(req)
    print(res.read().decode('utf-8'))
