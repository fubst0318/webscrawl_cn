#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这是使用Queue 实现Process间的通信演示
'''

from multiprocessing import Process, Queue
import time
import random
import os


def write(q):
    # 写数据进程执行的代码
    for value in ['A', 'B', 'C']:
        print('Put {0} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    # 读数据进程执行的代码
    while True:
        value = q.get(True)
        print('Get {0} from queue.'.format(value))


if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程:
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw,写入:
    pw.start()
    # 启动子进程pr,读取:
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
