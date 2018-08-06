#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
这里使用另一个图片再次识别一次
使用tesserocr识别
"""

import tesserocr
from PIL import Image

if __name__ == '__main__':
    image = Image.open('code.jpg')
    result = tesserocr.image_to_text(image)
    print(result)
