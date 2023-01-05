class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        index = len(self.items) - 1
        if index == -1:
            index = 0
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] > item:
                index = i
        self.items.insert(index, item)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def display(self):
        for element in self.items:
            print(element)



