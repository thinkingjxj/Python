import queue
import threading


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_worker(item)
        q.tast_done()


q = queue.Queue()
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for item in source():
    q.put(item)

q.join()

for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()
