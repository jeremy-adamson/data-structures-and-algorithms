from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self, root = None):
        super().__init__(root)

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        previous = None

        while current:
            if current.value < value:
                previous = current
                current = current.left
                if not current:
                    previous.left = Node(value)
                    break
            elif current.value >= value:
                previous = current
                current = current.right
                if not current:
                    previous.right = Node(value)
                    break


    def contains(self, value):
        current = self.root

        while not current.value == value:
            if current.value < value:
                current = current.left
            elif current.value > value:
                current = current.right

            if not current:
                return False

        return True

