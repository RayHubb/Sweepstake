class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        print(self.stack[-1].name)
        return self.stack.pop(-1)
