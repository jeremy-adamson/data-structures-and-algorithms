from data_structures.stack import Stack
from data_structures.stack import Node


class PseudoQueue:
    def __init__(self):
        self.stackmain = Stack()
        self.stackaux = Stack()

    def enqueue(self, value):
        self.stackmain.push(value)

        if self.stackaux.is_empty():
            self.stackaux.push(self.stackmain.top)
            return

        traverse = self.stackaux.top
        while traverse.next:
            traverse = traverse.next
        traverse.next = Node(self.stackmain.top)


    def dequeue(self):
        if self.stackmain.is_empty():
            raise Exception("Queue is empty")

        value = self.stackaux.pop().value
        self.stackaux.top().next = None
        return value
