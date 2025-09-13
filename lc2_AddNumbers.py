from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
This is the solution that I figured out on my own using a list reversal and stuff.
Gemini suggested the solution below which is far more efficient.

runtime: O(n + m)
space: O(max(n,m))
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse the two lists
        i = 0
        total = 0
        while l1 and l2:
            total += (l1.val + l2.val) * (10 ** i)
            i += 1
            l1 = l1.next
            l2 = l2.next
        if l1 and not l2:
            while l1:
                total += l1.val * (10**i)
                i += 1
                l1 = l1.next
        elif not l1 and l2:
            while l2:
                total += l2.val * (10**i)
                i += 1
                l2 = l2.next
        if total == 0:
            return ListNode(val=0)
        new_node, prev = None, None
        while total > 0:
            new_node = ListNode(val=total%10, next=prev)
            prev = new_node
            total = total // 10
        return self.rev_list(new_node)
        
    def rev_list(self, l):
        prev = None
        curr = l
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        curr = prev
        return curr
    

'''
runtime: O(n + m)
space: O(max(n,m))
'''
class GeminiSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the construction of the new list
        dummy = ListNode()
        current = dummy
        carry = 0

        # Loop through both lists until both are empty
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10

            # Create a new node with the calculated digit and add it to the result list
            current.next = ListNode(new_digit)

            # Move pointers to the next nodes/carry
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # The result is the node after the dummy node
        return dummy.next