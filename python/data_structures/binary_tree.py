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

    def find_maximum_value(self):
        if not self.root:
            return None
        else:
            current_node = self.root
            return self._max_value_helper_(current_node)

    def _max_value_helper_(self, current_node):
        maxValue = current_node.value

        if current_node.left:
            left = self._max_value_helper_(current_node.left)
            if left > maxValue:
                maxValue = left
        if current_node.right:
            right = self._max_value_helper_(current_node.right)
            if right > maxValue:
                maxValue = right

        return maxValue


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
