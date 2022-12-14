# implementing queues in python

from collections import deque
from heapq import heappop, heappush

class Iterable:
    def __len__(self):
        return len(self.elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(Iterable):
    def __init__(self, *elements):
        self.elements = deque(elements)

    def enqueue(self, element):
        self.elements.append(element)

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue:
    def __init__(self):
        self.elements = []
