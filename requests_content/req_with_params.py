#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

data = {
    'name': 'tonyxu',
    'age': 20
}

if __name__ == '__main__':

    res = requests.get('http://httpbin.org/get', params=data)
    print(type(res.text))
    print(res.json())
    print(type(res.json()))
