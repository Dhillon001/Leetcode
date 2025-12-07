# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # 1. Find the middle (slow ends at mid)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Reverse second half starting at slow
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev now points to head of reversed second half
        
        # 3. Compare first half and reversed second half
        first, second = head, prev
        while second:  # only need to check second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True