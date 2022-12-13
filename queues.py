# implementing queues in python

from collections import deque

class Queue:
    def _init_(self, *elements):
        self.elements = deque(elements)
    
    def _len_(self):
        return len(self._elements)

    def _iter_(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self.elements.append(element)

    def dequeue(self):
        return self.elements.popleft()

