class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        return self._pre_order_helper_(self.root)

    def _pre_order_helper_(self, current):
        valueArray = []
        if current:
            valueArray += current.value
            valueArray += self._pre_order_helper_(current.left)
            valueArray += self._pre_order_helper_(current.right)

        return valueArray

    def in_order(self):
        return self._in_order_helper_(self.root)

    def _in_order_helper_(self, current):
        valueArray = []
        if current:
            valueArray += self._in_order_helper_(current.left)
            valueArray += current.value
            valueArray += self._in_order_helper_(current.right)

        return valueArray

    def post_order(self):
        return self._post_order_helper_(self.root)

    def _post_order_helper_(self, current):
        valueArray = []
        if current:
            valueArray += self._post_order_helper_(current.left)
            valueArray += self._post_order_helper_(current.right)
            valueArray += current.value

        return valueArray


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
