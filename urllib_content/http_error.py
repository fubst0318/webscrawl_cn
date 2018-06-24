#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        res = urlopen('http://www.123.com/tonyxu')
    except HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
