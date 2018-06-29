#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
beautifulSoup 兄弟节点信息的获取
主要是 前一个兄弟节点，后一个兄弟节点，前兄弟节点们，后兄弟节点们
'''

from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
"""

if __name__ == '__main__':
    bsObj = BeautifulSoup(html, 'lxml')
    print('Next Sibling: ', bsObj.a.next_sibling)
    print('Prev Sibling: ', bsObj.a.previous_sibling)
    print('Next Siblings: ', list(enumerate(bsObj.a.next_siblings)))
    print('Prev Siblings: ', list(enumerate(bsObj.a.previous_siblings)))
