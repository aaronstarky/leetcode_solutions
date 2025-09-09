# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list in half
        f, s = head, head
        while f is not None and f.next is not None:
            f = f.next.next
            s = s.next
        l2 = s.next
        s.next = None
        l1 = head
        # reverse the second list
        prev = None
        current = l2

        while current:
            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        l2 = prev
        while l1 and l2:
            temp1 = l1.next
            l1.next = l2
            temp2 = l2.next
            l2.next = temp1
            l1 = temp1        
            l2 = temp2