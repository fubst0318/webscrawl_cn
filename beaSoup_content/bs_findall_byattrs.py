#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
主要演示如何用fina_all的attrs来指定属性，查找相应内容 
find_all(name , attrs , recursive , text , **kwargs)
'''

from bs4 import BeautifulSoup

html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
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
    print(bsObj.find_all(attrs={'id': 'list-1'}))
    print(bsObj.find_all(attrs={'name': 'elements'}))
