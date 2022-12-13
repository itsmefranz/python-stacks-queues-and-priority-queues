# implementing queues in python

from collections import deque

class Iterable:
    def _len_(self):
        return len(self.elements)

    def _iter_(self):
        while len(self) > 0:
            yield self.dequeue()
