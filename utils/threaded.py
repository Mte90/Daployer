from threading import Thread
from queue import Queue


def threaded(fn):
    def call(*args, **kwargs):
        job = Thread(target=fn, args=args,
                     kwargs=kwargs)
        job.start()
        return job

    return call


def threaded_with_queue(fn):
    def wrap(queue, *args, **kwargs):
        queue.put(fn(*args, **kwargs))

    def call(*args, **kwargs):
        queue = Queue()
        job = Thread(target=wrap, args=(queue,) + args,
                     kwargs=kwargs)
        job.start()
        job.join()
        return queue.get()

    return call
