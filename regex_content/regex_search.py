#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
re.match()匹配是从字符串的开头开始匹配，一旦开头不匹配，那么整个匹配就失败。
import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo', content)
print(result)

这种返回的结果就是 None

另一种匹配的模式是,re.search(),这个在匹配时会扫描整个字符串，然后返回第一个匹配成功的结果。
如果搜索完了还没有找到，则返回None
'''

import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
regexM = re.compile(r'Hello.*?(\d+).*?Demo')
result = re.search(regexM, content)
print(result)
