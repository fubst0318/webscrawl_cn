#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import build_opener, HTTPCookieProcessor
from http.cookiejar import MozillaCookieJar


if __name__ == '__main__':
    filename = 'cookies.txt'
    cookie = MozillaCookieJar(filename)
    handler = HTTPCookieProcessor(cookie)
    opener = build_opener(handler)
    res = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)
