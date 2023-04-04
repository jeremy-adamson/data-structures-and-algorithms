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
            return_str+="{ " + current.value + " } -> "
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


class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class TargetError:
    pass
