#!/usr/bin/env python3

import threading
import time

def worker(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        time_point = time.ctime(time.time())
        thread_id = threading.get_native_id()
        print(f"thread: {name}, {thread_id} {time_point}")

t1 = threading.Thread(target=worker, args=('thread1',1,))
t2 = threading.Thread(target=worker, args=('thread2',2,))

t1.start()
t2.start()

threads_count = threading.active_count()
print(f'Active threads {threads_count}.')

t1.join()
t2.join()

print('thread1 alive?', t1.is_alive())
print('thread2 alive?', t2.is_alive())
