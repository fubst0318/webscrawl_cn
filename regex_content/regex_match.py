#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里主要演示 加上()的精准匹配
'''

import re

if __name__ == '__main__':
    content = 'Hello 1234567 World_This is a Regex Demo'
    regexM = re.compile(r'^Hello\s(\d+)\sWorld')
    result = re.match(regexM, content)
    print(result)
    print(result.group())
    print(result.group(1))
    print(result.span())
