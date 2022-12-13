# implementing queues in python

from collections import deque

class Iterable:
    def _len_(self):
        return len(self.elements)

    def _iter_(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(Iterable):
    def _init_(self, *elements):
        self.elements = deque(elements)

    def enqueue(self, element):
        self.elements.append(element)

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

