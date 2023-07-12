from data_structures.binary_tree import BinaryTree, Node


def tree_intersection(tree_1, tree_2):
    hash_map_1 = fill_hashmap(tree_1)
    hash_map_2 = fill_hashmap(tree_2)
    intersection = []

    for value, if_in in hash_map_1.items():
        if value in hash_map_2:
            intersection.append(value)

    return intersection


def fill_hashmap(tree_root):
    hash_map = {}
    traversal_list = []
    traversal_list.append(tree_root.root)

    while any(traversal_list):
        current_node = traversal_list.pop(0)
        if current_node.left:
            traversal_list.append(current_node.left)
        if current_node.right:
            traversal_list.append(current_node.right)
        hash_map[current_node.value] = True

    return hash_map


