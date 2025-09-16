# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        max_depth = 0
        stack.append((root, 1))
        while len(stack) > 0:
            item = stack.pop()
            if item[0] is None:
                continue
            max_depth = max(item[1], max_depth)
            stack.append((item[0].left, item[1] + 1))
            stack.append((item[0].right, item[1] + 1))
        return max_depth
