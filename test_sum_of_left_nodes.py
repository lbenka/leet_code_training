from typing import Optional
import pytest 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def is_leaf(node: TreeNode):
            return node.left is None and node.right is None

        def process_node(node: TreeNode):
            r = 0

            if node.left:
                if is_leaf(node.left):
                    r += node.left.val
                else:
                    r += process_node(node.left)

            if node.right:
                if not is_leaf(node.right):
                    r += process_node(node.right)

            return r

        if root.left is None and root.right is None:
            return 0

        return process_node(root)


@pytest.mark.parametrize(
    "input, output",
    [
        (
            TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))),
            24,
        ),
        (TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)), right=TreeNode(val=3)), 4),
        (TreeNode(val=1), 0),
    ],
)
def test_solution(input, output):
    assert Solution().sumOfLeftLeaves(input) == output
