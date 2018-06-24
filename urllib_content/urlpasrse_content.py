#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from urllib.parse import urlunparse, urlsplit, urlencode

if __name__ == '__main__':
    '''
    这是urlunparse的例子
    '''
    data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
    print(urlunparse(data))
    '''
    这是urlsplit的例子
    '''
    res = urlsplit('http://www.baidu.com/index.html:user?id=6#comment')
    print(type(res), res, sep='\n')
    '''
    这是urlencode的例子
    '''
    params = {
        'name': 'tonyxu',
        'age': 22
    }
    base_url = 'http://www.baidu.com?'
    url = base_url + urlencode(params)
    print('urlencode:' + url)
