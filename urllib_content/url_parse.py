#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.parse import urlparse

if __name__ == '__main__':
    '''
    1.这是一个初始例子
    res = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
    print(type(res), res, sep='\n')
    '''
    '''
    2.这是一个设定scheme的例子
    
    res = urlparse(
        'http://www.baidu.com/index.html;user?id=5#comment', scheme='https')
    print(type(res), res, sep='\n')
    '''
    '''
    3.这是一个allow_fragment = False的例子
    '''
    res = urlparse(
        'http://www.baidu.com/index.html;user?id=5#comment', allow_fragments=False)
    print(type(res), res, sep='\n')
