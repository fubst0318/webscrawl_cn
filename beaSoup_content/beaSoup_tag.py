#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
选取节点的特定元素
'''

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

if __name__ == '__main__':
    bsObj = BeautifulSoup(html, 'lxml')
    print(bsObj.title)
    print(type(bsObj.title))
    print(bsObj.title.string)
    print(bsObj.head)
    print(bsObj.p)
    '''
    获取属性名称 name 属性来获取节点的名称
    '''
    print('属性名称:', bsObj.title.name)
    '''
    获取属性 每个节点可能有多个属性，比如 id，class 等等，
    我们选择到这个节点元素之后，可以调用 attrs 获取所有属性。
    '''
    print('第一个p节点的所有属性:', bsObj.p.attrs)
    print('第一个p节点的name属性', bsObj.p.attrs['name'])
    '''
    更简单的数据获取方式，不写attrs，直接节点元素后面加中括号，传入属性名就可以达到属性值了：
    '''
    print('更简单的name数据获取方式:', bsObj.p['name'])
    print('更简单的class数据获取方式:', bsObj.p['class'])
