class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def display(self):
        for element in self.items:
            print(element)

