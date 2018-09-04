#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
调度模块
主要作用是将前述几个功能粘合起来一起使用
"""

import time
from multiprocessing import Process
from api import app
from config import *
from tester import *

class Scheduler(object):
    pass