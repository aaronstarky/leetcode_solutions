# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        self.dfs(root)
        return self.balanced
    
    def dfs(self, node):
        if not node or not self.balanced:
            return 0
        l_height = self.dfs(node.left)
        r_height = self.dfs(node.right)
        if abs(r_height - l_height) > 1:
            self.balanced = False
        return max(l_height, r_height) + 1

        