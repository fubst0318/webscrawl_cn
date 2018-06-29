#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里主要演示beautifulSoup的父节点的查找
'''

from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <p class="story">
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
        </p>
"""

if __name__ == '__main__':
    bsObj = BeautifulSoup(html, 'lxml')
    print(bsObj.a.parent)  # 这里获取的是a的父节点
    print(type(bsObj.a.parents))  # 这里获取的是所有祖先节点，返回的是一个迭代器
    for i, parent in enumerate(bsObj.a.parents):  # 这里对祖先节点进行遍历
        print(i, parent)
