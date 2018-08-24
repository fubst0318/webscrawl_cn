#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pickle import dumps, loads
from redis import StrictRedis
from weixin.request import WeixinRequest
from weixin.config import REDIS_HOST, REDIS_KEY, REDIS_PASSWORD, REDIS_PORT

"""
这里主要使用Redis中的List
用的是rpush,lpop命令
"""


class RedisQueue():
    def __init__(self):
        """
        初始化Redis
        """
        self.db = StrictRedis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

    def add(self, request):
        """
        向队列添加序列化后的Request
        :param request: 请求对象
        :param fail_time : 失败次数
        :return: 添加结果
        """
        if isinstance(request, WeixinRequest):
            return self.db.rpush(REDIS_KEY, dumps(request))
        return False

    def pop(self):
        """
        取出下一个Request 并反序列化
        :return: Request or None
        """
        if self.db.llen(REDIS_KEY):
            return loads(self.db.lpop(REDIS_KEY))
        else:
            return None

    def empty(self):
        return self.db.llen(REDIS_KEY) == 0


if __name__ == '__main__':
    db = RedisQueue()
    start_url = 'http://www.baidu.com'
    weixin_request = WeixinRequest(
        url=start_url, callback='hello', need_proxy=True)
    db.add(weixin_request)
    request = db.pop()
    print(request)
    print(request.callback, request.need_proxy)
