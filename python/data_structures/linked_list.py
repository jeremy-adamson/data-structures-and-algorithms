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
    """
    Basic structure within a linked list
    """

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class TargetError:
    pass

def zipLists(list1, list2):
    combined = LinkedList()
    traverse1 = list1.head
    traverse2 = list2.head

    if traverse1:
        combined.head = Node(traverse1.value)
        zipper = combined.head
        traverse1 = traverse1.next
        if traverse2:
            zipper.next = Node(traverse2.value)
            zipper = zipper.next
            traverse2 = traverse2.next
    elif traverse2:
        combined.head = Node(traverse2.value)
        zipper = combined.head
        traverse2 = traverse2.next

    while traverse1 or traverse2:
        if traverse1:
            zipper.next = Node(traverse1.value)
            zipper = zipper.next
            traverse1 = traverse1.next

        if traverse2:
            zipper.next = Node(traverse2.value)
            zipper = zipper.next
            traverse2 = traverse2.next

    return combined



