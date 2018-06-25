#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里演示的主要是如何获取图片、音频、视频文件
保存到本地的方法
'''

import requests

if __name__ == '__main__':
    res = requests.get('https://github.com/favicon.ico')
    # print(res.text) 这个内容是一个字符串
    # print(res.content) 这个内容是一个二进制的字节流
    with open('favicon.ico', 'wb') as f:
        f.write(res.content)
