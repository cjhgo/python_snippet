#coding: utf-8
#created at 17-2-24 16:06

import time
from threading import Thread
from Queue import Queue

def do_work(item):
    print "doing..."
    time.sleep(0.5)
    print "end,,,,"

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()
    print "????"

q = Queue()
for i in range(2):
     t = Thread(target=worker)
     t.daemon = True
     t.start()

for item in range(10):
    q.put(item)

q.join()
print "????"
q.put(55)

from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=2)


@gen.coroutine
def consumer():
    while True:
        item = yield q.get()
        try:
            print('Doing work on %s' % item)
            yield gen.sleep(0.01)
        finally:
            q.task_done()


@gen.coroutine
def producer():
    for item in range(5):
        yield q.put(item)
        print('Put %s' % item)


@gen.coroutine
def main():
    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    yield producer()  # Wait for producer to put all tasks.
    yield q.join()  # Wait for consumer to finish all tasks.
    print('Done')


IOLoop.current().run_sync(main)