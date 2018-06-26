#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
正则表达式入门，这里主要用re.match()
'''

import re

if __name__ == '__main__':
    content = 'Hello 123 4567 World_This is a Regex Demo'
    print(len(content))
    result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
    print(result)
    print(result.group())
    print(result.span())
