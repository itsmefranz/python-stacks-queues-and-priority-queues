# queues.py

from collections import deque

class Queue:
    def _init_(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def deque(self):
        return self._elements.popleft()