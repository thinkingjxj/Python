import threading
import time
import logging
threading.Timer
FORMAT = ""
logging.basicConfig(level=logging.INFO, format=FORMAT)

def foo(n):
    for i in range(n):
        print(i)
        time.sleep(1)
# 调换10和20看看效果
t = threading.Thread(target=foo, args=(20,), daemon=True)
t.start()

t1 = threading.Thread(target=foo, args=(10,), daemon=False)
t1.start()

time.sleep(2)
print('Main Thread Exiting')




