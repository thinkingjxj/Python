import os, time, random
from multiprocessing import Pool


def long_time_tast(name):
    print('Run task {} ({})'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task {} runs {} seconds'.format(name, (end - start)))

if __name__ == '__main__':
    print('Parent process {}'.format(os.getpid()))
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_tast, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done')
