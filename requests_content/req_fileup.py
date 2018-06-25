#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里主要是使用requests 的文件上传功能
'''

import requests

if __name__ == '__main__':
    files = {'file': open('favicon.ico', 'rb')}
    res = requests.post('http://httpbin.org/post', files=files)
    print(res.text)
