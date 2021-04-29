from data_queue import Queue


class QueueManager:
    def __init__(self):
        self.queue = Queue()

    def inset_sweepstake(self, sweepstake):
        self.queue.enqueue(sweepstake)

    def get_sweepstake(self):
        self.queue.dequeue()

