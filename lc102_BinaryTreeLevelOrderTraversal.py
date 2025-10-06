# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We're gonna do a breadth first search using a queue
        if root == []:
            return []
        q = queue.Queue()
        output = []
        curr_depth = 0
        q.put((root, depth))
        while not q.empty():
            curr, curr_depth = q.get()
            if curr is None:
                continue
            if curr_depth == len(output):
                output.append([curr.val])
            else:
                output[curr_depth].append(curr.val)
            if curr.left is not None:
                q.put((curr.left, curr_depth+1))
            if curr.right is not None:
                q.put((curr.right, curr_depth+1))
        return output
               