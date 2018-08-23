#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import asyncio
import aiohttp
import time
import sys
from setting import VALID_STATUS_CODES, TEST_URL, BATCH_TEST_SIZE
from db import RedisClient


class Tester(object):
    def __init__(self):
        self.redis = RedisClient()

    
    async def test_single_proxy(self,proxy):
        """
        测试单个代理
        :param proxy:单个代理
        :return: None
        """
        
