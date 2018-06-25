#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
本部分主要是熟悉关于反序列化、URL编码相关内容
'''
from urllib.parse import parse_qs, parse_qsl, quote, unquote

query = 'name=tonyxu&age=22'

if __name__ == '__main__':
    '''
    1.反序列化(字典格式)
    '''
    print('--------字典格式------')
    print(parse_qs(query))
    '''
    2.反序列化(元组格式)
    '''
    print('--------元组格式------')
    print(parse_qsl(query))
    '''
    3.URL编码
    '''
    keyword = '壁纸'
    url = 'https://www.baidu.com/s?wd=' + quote(keyword)
    print(url)
    '''
    4.URL解码
    '''
    print(unquote(url))
