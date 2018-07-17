#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
这是一个multiprocessing的使用Pool的案例
'''

import os
import time
import random
from multiprocessing import Pool


def long_time_task(name):
    print('Run task {0} ({1})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {0} runs {1}'.format(name, end - start))


if __name__ == '__main__':
    print('Parent process {0}'.format(os.getpid()))
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesss done.')
