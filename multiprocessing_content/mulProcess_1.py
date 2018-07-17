#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这是一个multiprocessing的另一个Process的案例
与上个例子类似，这是另一个案例的一个例子，复习下
'''

import os
from multiprocessing import Process


def run_proc(name):
    # 子进程需要执行的代码
    print('Run child process {0} ({1})...'.format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {0}.'.format(os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('Process will start.')
    p.start()
    p.join()
    print('Process end.')
