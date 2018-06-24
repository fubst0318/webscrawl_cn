#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import URLError


if __name__ == '__main__':
    try:
        res = urlopen('http://www.123.com/tonyxu')
    except URLError as e:
        print(e.reason)
