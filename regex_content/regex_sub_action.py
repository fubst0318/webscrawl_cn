#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这里首先演示下利用正则表达式的sub方法
re.sub()的另一个实例
这个例子是先把部分冗余的数据替换掉，然后获取替换后文件的文本值
'''

import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

if __name__ == '__main__':
    html = re.sub(r'<a.*?>|</a>', '', html)
    print(html)
    results = re.findall(r'<li.*?>(.*?)</li>', html, re.S)
    for result in results:
        print(result.strip())
