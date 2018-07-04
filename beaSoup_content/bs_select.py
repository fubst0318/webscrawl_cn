#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里演示bs4使用css选择器的情况
'''

from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''

if __name__ == '__main__':
    bsObj = BeautifulSoup(html, 'lxml')
    # print(bsObj.select('.panel .panel-heading'))
    # print(bsObj.select('ul li'))
    # print(bsObj.select('#list-2 .element'))
    print(type(bsObj.select('ul')[0]))
