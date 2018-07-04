#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里演示findall方法的text项
find_all(name , attrs , recursive , text , **kwargs)
这里面用了re.compile,正则表达式
'''

from bs4 import BeautifulSoup
import re

html = '''
<div class="panel">
    <div class="panel-body">
        <a>Hello, this is a link</a>
        <a>Hello, this is a link, too</a>
    </div>
</div>
'''

if __name__ == '__main__':
    bsObj = BeautifulSoup(html, 'lxml')
    print(bsObj.find_all(text=re.compile('link')))
