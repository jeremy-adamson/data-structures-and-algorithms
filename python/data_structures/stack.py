from data_structures.invalid_operation_error import InvalidOperationError

class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return not bool(self.top)

class Node:
    def __init__(self, data = None, next_node = None):
        self.value = data
        self.next = next_node
