from data_stack import Stack


class StackManager:
    def __init__(self):
        self.stack = Stack()

    def insert_sweepstake(self, sweepstake):
        self.stack.push(sweepstake)

    def get_sweepstake(self):
        self.stack.pop()
