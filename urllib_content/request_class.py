#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
相比直接调用urlopen,Request类可以传递更多的参数，比如Headers等信息
'''
from urllib.request import Request
from urllib.request import urlopen

if __name__ == '__main__':
    req = Request('https://www.python.org/')
    res = urlopen(req)
    print(res.read().decode('utf-8'))
