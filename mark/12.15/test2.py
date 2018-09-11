import threading


def add(x, y):
    print(x + y)


def worker():
    print("t's daemon = {}".format(threading.current_thread().isDaemon()))
    t1 = threading.Thread(target=add)
    t1.start()
    print('ending')

t = threading.Thread(target=worker, daemon=True)
t.start()