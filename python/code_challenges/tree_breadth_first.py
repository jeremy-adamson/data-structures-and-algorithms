from data_structures.binary_tree import BinaryTree, Node


def breadth_first(tree):
    main_list = []
    values = []
    if not tree.root:
        return []

    main_list.append(tree.root)

    while len(main_list) > 0:
        current_node = main_list.pop(0)
        if current_node.left:
            main_list.append(current_node.left)
        if current_node.right:
            main_list.append(current_node.right)
        values.append(current_node.value)

    return values

