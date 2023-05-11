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

        while True:
            if current.value < value:
                if not current.left:
                    current.left = Node(value)
                    return
                current = current.left
            elif current.value >= value:
                if not current.right:
                    current.right = Node(value)
                    return
                current = current.right


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

