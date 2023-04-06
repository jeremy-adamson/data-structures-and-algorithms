class LinkedList:
    """
    Construction of a linked list data structure with methods for adding elements and returning a string with current elements
    Input: Data of any data type through insert()
    Output: String through __str__() and boolean from includes()
    """

    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
    def __str__(self):
        current = self.head

        return_str = ""

        while current:
            return_str+="{ " + str(current.value) + " } -> "
            current = current.next

        return_str+="NULL"

        return return_str

    def includes(self, value):
        if not value:
            return False

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data)

    def insert_before(self, value, data):

        if not self.head:
            return

        if self.head.value == value:
            self.head = Node(data, self.head)
            return

        current = self.head

        while current.next.value != value:
            current = current.next
            if not current.next:
                return

        current.next = Node(data, current.next)

    def insert_after(self, value, data):
        if not self.head:
            return

        current = self.head

        while current.value != value:
            current = current.next
            if not current:
                return

        current.next = Node(data, current.next)




class Node:
    """
    Basic structure within a linked list
    """

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class TargetError:
    pass
