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

    def kth_from_end(self, k):
        if not self.head:
            raise TargetError

        places = []
        current = self.head

        while current:
            places.append(current)
            current = current.next

        index = len(places) - k - 1

        if index < 0 or index > len(places) - 1:
            raise TargetError

        return places[index].value


class Node:
    """
    Basic structure within a linked list
    """

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class TargetError(Exception):
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



