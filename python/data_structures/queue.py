class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, value):
        if not self.back:
            self.front = Node(value)
            self.back = self.front
        self.back.next = Node(value)
        self.back = self.back.next

    def dequeue(self):
        if not self.front:
            raise Exception("Empty Queue")
        value = self.front.value
        self.front = self.front.next
        return value

    def peek(self):
        if not self.front:
            raise Exception("Empty Queue")
        return self.front.value

    def is_empty(self):
        return bool(self.front)

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
