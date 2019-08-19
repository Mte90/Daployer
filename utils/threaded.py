from threading import Thread
from queue import Queue


def threaded(fn):
    def wrap(queue, *args, **kwargs):
        queue.put(fn(*args, **kwargs))

    def call(*args, **kwargs):
        queue = Queue()
        job = Thread(target=wrap, args=(queue,) + args,
                     kwargs=kwargs)
        job.start()
        return queue.get()

    return call
