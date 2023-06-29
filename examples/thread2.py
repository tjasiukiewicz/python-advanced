#!/usr/bin/env python3

import threading
import time

data = []

def worker(lock, data, value):
    count = 0
    while count < 50:
        time.sleep(0.1)
        lock.acquire()
        data.append(value)
        lock.release()
        count += 1

lock = threading.Lock()
t1 = threading.Thread(target=worker, args=(lock, data, 1,))
t2 = threading.Thread(target=worker, args=(lock, data, 2,))

t1.start()
t2.start()

t1.join()
t2.join()

print(data)
