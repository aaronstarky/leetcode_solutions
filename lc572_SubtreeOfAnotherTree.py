# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # binary search search until val of subtree is found
        # if not found
            # return false
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                if self.same_tree(node, subRoot):
                    return True
            stack.append(node.left)
            stack.append(node.right)          
        return False
        
    def same_tree(self, t1, t2):
        tree1 = [t1]
        tree2 = [t2]
        while len(tree1) > 0 and len(tree2) > 0:
            t1 = tree1.pop()
            t2 = tree2.pop()
            if not t1 and not t2:
                continue
            if (not t1 and t2) or (t1 and not t2) or (t1.val != t2.val):
                return False
            tree1.append(t1.left)
            tree1.append(t1.right)
            tree2.append(t2.left)
            tree2.append(t2.right)
        if len(tree1) != len(tree2):
            return False
        return True

