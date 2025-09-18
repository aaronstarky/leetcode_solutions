from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = [p]
        tree2 = [q]
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



        