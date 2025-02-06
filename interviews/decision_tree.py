from dataclasses import dataclass
"""
Y

  	     X1 < 3
     X2 < 4	     Y
 N		Y	
"""

@dataclass
class DecisionTreeNode:
    value: int = None
    signal: str = None
    constant: int = None
    left: 'DecisionTreeNode' = None
    right: 'DecisionTreeNode' = None


def set_node_split(node, signal, constant):
    node.left = DecisionTreeNode('N')
    node.right = DecisionTreeNode('N')
    node.signal = signal
    node.constant = constant

    return node.left, node.right


def set_leaf_value(leaf, value):
    leaf.value = value


def evaluate(root, signals):
    curr = root
    while curr.left is not None:
        val = signals[curr.signal]
        if val < curr.constant:
            curr = curr.left
        else:
            curr = curr.right
    return curr.value


root = DecisionTreeNode()
left, right = set_node_split(root, 'X1', 3)
set_leaf_value(right, 'Y')
level2_left, level2_right = set_node_split(left, 'X2', 4)
set_leaf_value(level2_right, 'Y')
evaluate(root, {'X1': 2, 'X2': 1})
