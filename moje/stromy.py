class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return f'\nNode {self.data} with children: {self.children}'

    __repr__ = __str__

def tree_depth(node: Node) -> int:
    if not node.children:
        return 0
    else:
        max_child_depth = 0
        for child in node.children:
            child_depth = tree_depth(child)
            if child_depth > max_child_depth:
                max_child_depth = child_depth
        return max_child_depth + 1

# Testy:
g_subtree = Node('G')
g_subtree.add_child(Node('H'))
g_subtree.add_child(Node('I'))

c_subtree = Node('C')
c_subtree.add_child(g_subtree)

b_subtree = Node('B')
b_subtree.add_child(Node('D'))
b_subtree.add_child(Node('E'))
b_subtree.add_child(Node('F'))

tree = Node('A')
tree.add_child(b_subtree)
tree.add_child(c_subtree)

print(tree_depth(tree))  # 3
