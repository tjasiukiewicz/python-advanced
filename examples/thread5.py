#!/usr/bin/env python3

import concurrent.futures
import time

def worker(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        time_point = time.ctime(time.time())
        print(f"{name}: {time_point}")

my_thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

my_thread_pool.submit(worker, 'thread1', 1)
my_thread_pool.submit(worker, 'thread2', 2)

my_thread_pool.shutdown(wait=True)
