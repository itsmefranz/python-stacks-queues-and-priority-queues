# implementing queues in python

from collections import deque

class Queue:
    def _init_(self):
        self.elements = deque()

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.popleft()