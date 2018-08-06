#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
这里使用tesserocr 来自动识别验证码
"""

import tesserocr
from PIL import Image

if __name__ =='__main__':
    image = Image.open('yanzhen.jpg')
    result = tesserocr.image_to_text(image)
    print(result)