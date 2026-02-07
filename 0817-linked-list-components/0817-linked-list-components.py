# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        curr = head

        while curr:
            if curr.val in nums_set and (curr.next is None or curr.next.val not in nums_set):
                count += 1
            curr = curr.next

        return count
