#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from requests import get

if __name__ == '__main__':
    res = get('http://www.baidu.com')
    print(type(res))
    print(res.status_code)
    print(type(res.text))
    print(res.text)
    print(res.cookies)
