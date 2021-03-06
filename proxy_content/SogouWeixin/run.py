#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
实现该功能的主要要点如下：
1.修改代理池检测链接为搜狗微信站点
2.构建Redis爬取队列，用队列实现请求的存取
3.实现异常处理，失败的请求重新加入队列
4.实现翻页和提取文章列表，并把对应请求加入队列
5.实现微信文章信息的提取
6.将提取到的信息保存到MySQL
"""
