from data_structures.stack import Stack
from data_structures.stack import Node
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.stackmain = Stack()
        self.stackaux = Stack()

    def enqueue(self, value):
        self.stackmain.push(value)

        if self.stackaux.is_empty():
            self.stackaux.top = Node(self.stackmain.top)
            return

        traverse = self.stackaux.top
        while traverse.next:
            traverse = traverse.next
        traverse.next = Node(self.stackmain.top)


    def dequeue(self):
        if self.stackmain.is_empty():
            raise InvalidOperationError("Queue is empty")

        value = self.stackaux.pop().value
        print(value)
        print(self.stackaux.top)

        if self.stackaux.is_empty():
            self.stackmain.top = None
            return value

        self.stackaux.top.next = None
        return value
