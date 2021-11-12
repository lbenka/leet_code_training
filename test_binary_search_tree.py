import pytest


class Node:
    def __init__(self, data, left=None, right=None):
        self.val = data
        self.data = data
        self.left = left
        self.right = right


def check_binary_search_tree(root: Node) -> bool:
    def is_valid(node):
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False
        return True

    def process_node(root):
        result_left, result_right = True, True

        if root.left:
            if not is_valid(root):
                return False

            result_left = process_node(root.left)

        if root.right:
            if not is_valid(root):
                return False

            result_right = process_node(root.right)

        return all([result_right, result_left])  # todo: wtf

    return process_node(root)


@pytest.mark.parametrize(
    "inp, out",
    [
        (Node(7, left=Node(4, left=Node(3), right=Node(5)), right=Node(8, left=Node(6), right=Node(9))), True),
        (Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7))), False),
        (Node(5, left=Node(4, None, None), right=Node(6, left=Node(3), right=Node(7))), False),
    ],
)
def test_bst(inp, out):
    assert check_binary_search_tree(inp) == out
