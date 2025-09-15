# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        use a stack
        add the root
        get node from stack
        switch l and r child
        push them to stack
        '''
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node is None:
                continue
            temp = node.right
            node.right = node.left
            node.left = temp
            stack.append(node.right)
            stack.append(node.left)
        return root
        