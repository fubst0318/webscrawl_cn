#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里验证下非贪婪匹配的方法
.* 组合可以匹配非换行的字符任意多次
.*? 组合起来可以对字符结合整个表达式进行非贪婪匹配
'''

import re

if __name__ == '__main__':
    content = 'Hello 1234567 World_This is a Regex Demo'
    regexM = re.compile(r'He.*?(\d+).*Demo$')
    result = re.match(regexM, content)
    print(result)
    print(result.group(1))
