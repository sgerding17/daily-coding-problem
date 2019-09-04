#!/usr/bin/python3

# 2019-09-03
#
# Implement a job scheduler which takes in a function f and an integer n, and
# calls f after n milliseconds.

import threading
import time

def run_after_delay(f, delay):
    time.sleep(delay / 1000.)
    f()

threads = []
def schedule(f, delay):
    thread = threading.Thread(target=run_after_delay, args=[f, delay])
    thread.start()
    threads.append(thread)

def a(): print('a')
def b(): print('b')
def c(): print('c')

schedule(a, 1000)
schedule(b, 3000)
schedule(c, 2000)

for thread in threads:
    thread.join()
