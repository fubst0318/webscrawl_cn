#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里首先演示下利用正则表达式的sub方法
这里的使用是去除字符串中的所有数字，替换为空
'''

import re

content = '54aK54yr5oiR54ix5L2g'

if __name__ == '__main__':
    result = re.sub(r'\d+', '', content)
    print(result)
