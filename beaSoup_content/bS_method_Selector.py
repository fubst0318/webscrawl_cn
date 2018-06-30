#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里主要演示beautifulSoup的方法选择器
这里例子用节点名进行查询
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
    # print(bsObj.find_all(name='ul'))
    # print(type(bsObj.find_all(name='ul')[0]))
    for ul in bsObj.find_all(name='ul'):  # 这里演示了如何对选中的标签进行继续迭代
        # print(ul.find_all(name='li'))
        for li in ul.find_all(name='li'):
            print(li.string)
