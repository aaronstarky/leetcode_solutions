'''
This solution was given to me by Gemini and is probably the most efficient 
way to do the list reversal. I tried a stack based approach which is below
and it worked great, but had runtime issues.
'''
from typing import Optional

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = None
        curr = head
        while curr is not None:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev
    

# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#     if not head:
#         return None
#     stack = []
#     curr = head
#     while curr is not None:
#         stack.append(curr)
#         curr = curr.next
#     print(stack)
#     head = stack.pop()
#     curr = head
#     while len(stack) > 0:
#         print(len(stack))
#         curr.next = stack.pop()
#         curr = curr.next
#     return head

# fourth = ListNode(3, None)
# third = ListNode(2, fourth)
# second = ListNode(1, third)
# head = ListNode(0, second)

# print(reverseList(head))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next