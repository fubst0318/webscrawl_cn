#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
这里主要是微博手机版登录的路径识别图像验证
对应的网址为:'https://passport.weibo.cn/signin/login'
本次内容主要分2步
1.通过模拟频繁登录微博，来获取24张验证码图片
2.通过程序来识别24张验证码
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from PIL import Image
from io import BytesIO
from os import listdir
from selenium.webdriver import ActionChains

LoginName = 'tonylove0318@hotmail.com'
PassWord = '184932'

TEMPLATES_FOLDER = 'templates/'


class CrackWeibo():
    def __init__(self):
        self.url = 'https://passport.weibo.cn/signin/login'
        self.browser = webdriver.Chrome()
        self.LoginName = LoginName
        self.PassWord = PassWord
        self.wait = WebDriverWait(self.browser, 5)

    def __del__(self):
        self.browser.close()

    def open(self):
        print('连接微博')
        self.browser.get(self.url)
        # 获取登录信息
        Loginid = self.wait.until(
            EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(
            EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(
            EC.element_to_be_clickable((By.ID, 'loginAction')))
        Loginid.send_keys(self.LoginName)
        password.send_keys(self.PassWord)
        submit.click()

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img_flag = True
        while img_flag:
            try:
                img = self.wait.until(EC.presence_of_element_located(
                    (By.CLASS_NAME, 'patt-shadow')))
                print('图片信息', img)
                location = img.location
                size = img.size
                top, bottom, left, right = location['y'], location['y'] + \
                    size['height'], location['x'], location['x'] + size['width']
                img_flag = False
            except TimeoutException:
                print('未出现验证码')
                time.sleep(2)
                self.open()
        return (top, bottom, left, right)

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图像对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1:图片 1
        :param image2:图片 2
        :param x: 位置x 
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 20
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def same_image(self, image, template):
        """
        识别相似验证码
        :param image:带识别验证码
        :parma template:模板
        :return:
        """
        # 相似度阈值
        thresold = 0.99
        count = 0
        for x in range(image.width):
            for y in range(image.height):
                # 判断像素是否相同
                if self.is_pixel_equal(image, template, x, y):
                    count += 1
        result = float(count) / (image.width * image.height)
        if result > thresold:
            print('成功匹配')
            return True
        else:
            return False

    def detect_image(self, image):
        """
        匹配图片
        :param image：图片
        :return: 拖动顺序
        """
        for template_name in listdir(TEMPLATES_FOLDER):
            print('正在匹配', template_name)
            template = Image.open(TEMPLATES_FOLDER + template_name)
            if self.same_image(image, template):
                # 返回顺序
                numbers = [int(number)
                           for number in list(template_name.split('.')[0])]
                print('拖动顺序', numbers)
                return numbers

    def move(self, numbers):
        """
        根据顺序拖动
        :param numbers
        :return:
        """
        # 获取四个按点
        circles = self.browser.find_element_by_css_selector(
            '.patt-wrap .patt-circ')
        dx = dy = 0
        for index in range(4):
            circle = circles[numbers[index] - 1]
            # 如果是第一次循环
            if index == 0:
                # 点击第一个按点
                ActionChains(self.browser).move_to_element_with_offset(
                    circle, circle.size['width'] / 2, circle.size['height'] / 2).click_and_hold().perform()
            else:
                # 小幅移动
                times = 30
                # 拖动
                for i in range(times):
                    ActionChains(self.browser).move_by_offset(
                        dx / times, dy / times).perform()
                    time.sleep(1 / times)
            # 如果是最后一次循环
            if index == 3:
                # 松开鼠标
                ActionChains(self.browser).release().perform()
            else:
                # 计算下一次偏移
                dx = circles[numbers[index + 1] -
                             1].location['x'] - circle.location['x']
                dy = circles[numbers[index + 1] -
                             1].location['y'] - circle.location['y']

    def crack(self):
        """
        识别入口
        :return: 
        """
        self.open()
        # 获取验证码图片
        image = self.get_image('captcha.png')
        numbers = self.detect_image(image)
        self.move(numbers)
        time.sleep(10)
        print('识别结束')

    def main(self):
        """
        批量获取验证码
        :return: 图片对象
        """
        count = 0
        while True:
            self.open()
            self.get_image(str(count) + '.png')
            count += 1


if __name__ == '__main__':
    crack = CrackWeibo()
    crack.main()  # 这一步是获取图片
    # crack.crack() # 这一步是识别图片
