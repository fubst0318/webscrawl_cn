#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import URLError
import socket

if __name__ == '__main__':
    try:
        rep = urlopen('http://httpbin.org/get', timeout=0.1)
    except URLError as e:
        if isinstance(e.reason, socket.timeout):
            print('Time out!')
