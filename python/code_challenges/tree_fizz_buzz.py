from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):

    def depth_swap(current):
        current_value = None
        current_children = []

        if not current:
            return None

        if ((current.value)%15) == 0:
            current_value = 'FizzBuzz'
        elif ((current.value)%3) == 0:
            current_value = 'Fizz'
        elif ((current.value)%5) == 0:
            current_value = 'Buzz'
        else:
            current_value = str(current.value)

        for child in current.children:
            new_child = depth_swap(child)
            if new_child:
                current_children.append(new_child)

        new_node = Node(current_value)
        new_node.children = current_children
        return new_node


    fizzy_tree = KaryTree()

    if not tree.root:
        return fizzy_tree

    fizzy_tree.root = depth_swap(tree.root)

    return fizzy_tree




'''
class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children
'''
