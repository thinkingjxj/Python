import threading
import logging

threading.Timer

FORMAT = "%(asctime)-15s\t" \
         "Thread info: %(thread)d %(threadName)s %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

log1 = logging.getLogger('s')
log1.setLevel(logging.WARNING)

h1 = logging.StreamHandler()
h1.setLevel(logging.INFO)
fmt1 = logging.Formatter('log1-h1 %(message)s')
h1.setFormatter(fmt1)
log1.addHandler(h1)

log2 = logging.getLogger('s.s1')
print(log2.getEffectiveLevel())

h2 = logging.StreamHandler()
h2.setLevel(logging.ERROR)
fmt2 = logging.Formatter('log2-h2 %(message)s')
h2.setFormatter(fmt2)
log2.addHandler(h2)

log2.warning('log2 warning')
log2.error('log2 error')
log2.info('log2 info')
