class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentdNode = self.head
        while True:
            if currentdNode.nextNode is None:
                currentdNode.nextNode = node
                break
            currentdNode = currentdNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "-> ", end='')
            currentNode = currentNode.nextNode
        print("None")


if __name__ == "__main__":
    ll = LinkedList()
    ll.printLinkedList()
    ll.insert("3")
    ll.printLinkedList()
    ll.insert("44")
    ll.printLinkedList()
    ll.insert("55")
    ll.printLinkedList()
