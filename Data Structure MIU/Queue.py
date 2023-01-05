class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def len(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def clear(self):
        self._items = []
