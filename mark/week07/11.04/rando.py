import random
import datetime
import time

def source():
    while True:
        yield {'value': random.randint(1,100), 'datetime': datetime.datetime.now()}
        time.sleep(1)

def window(src, handler, width:int, interval:int):
    start = datetime.datetime.strptime('20170101 00:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    current = datetime.datetime.strptime('20170101 01:00:00 +0800', '%Y%m%d %H:%M:%S %z')
    buffer = []
    delta = datetime.timedelta(seconds=width - interval)
    while True:
        data = next(src)
        if data:
            buffer.append(data)
            current = data['datetime']
        if (current - start).total_seconds() >= interval:
            ret = handler(buffer)
            print('{:.2f}'.format(ret))
            start = current

            buffer = [x for x in buffer if x['datetime'] > current - delta]


def handler(iterable):
    vals = [x['values'] for x in iterable]
    return sum(vals) / len(vals)

window(source(), handler, 10, 5)
