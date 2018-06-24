#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from http.cookiejar import CookieJar
from urllib.request import HTTPCookieProcessor, build_opener

if __name__ == '__main__':
    cookie = CookieJar()
    handler = HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    res = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + '=' + item.value)
