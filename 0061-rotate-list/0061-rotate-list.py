# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        # 1. Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Reduce k
        k = k % length
        if k == 0:
            return head

        # 3. Make it circular
        tail.next = head

        # 4. Find new tail (length - k - 1)
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # 5. Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head