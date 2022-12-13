# queues.py

from collections import deque

class Queue:
    def _init_(self):
        self._elements = deque()