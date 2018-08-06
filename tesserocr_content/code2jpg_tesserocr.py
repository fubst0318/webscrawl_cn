#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
这里使用另一个图片识别一次
使用tesserocr识别
这里主要是要利用灰度、二值化来对图片进行处理
这个图例只是简单的使用 image 以及 image_to_text 会识别出来位FFKT
灰度、二值化处理后图片转换准确
"""

import tesserocr
from PIL import Image

if __name__ == '__main__':
    # image = Image.open('code2.jpg')
    # result = tesserocr.image_to_text(image)
    # print(result)
    image = Image.open('code2.jpg')
    image = image.convert('L')  # 转换灰度

    # 下面一段是进行二值化处理
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, '1')
    # 二值化处理结束
    result = tesserocr.image_to_text(image)
    print(result)
