import time
import threading


def bar():
    while True:
        time.sleep(1)
        print('bar')


def foo():
    print("t's daemon = {}".format(threading.current_thread().isDaemon()))
    t1 = threading.Thread(target=bar)
    t1.start()
    print("t1's daemon = {}".format(t1.isDaemon()))
    # t1.join()

t = threading.Thread(target=foo, daemon=True)
t.start()
# t.join()
# time.sleep(3)
print('Main Thread Exiting')
