# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.dfs(root)
        return self.max_diameter

    def dfs(self, node):
        if node is None:
            return 0
        l_height = self.dfs(node.left)
        r_height = self.dfs(node.right)
        current_diameter = l_height + r_height
        self.max_diameter = max(self.max_diameter, current_diameter)
        return max(l_height, r_height) + 1
