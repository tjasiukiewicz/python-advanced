#!/usr/bin/env python3

import threading
import time

def worker():
    print("I'm alive!'")

t = threading.Timer(5, worker)
t.start()

time.sleep(7)
t.cancel()
