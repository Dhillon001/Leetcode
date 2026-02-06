class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False

        i = 0

        # Phase 1: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        # Must have at least one increase
        if i == 0:
            return False
        p = i

        # Phase 2: strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        # Must have at least one decrease
        if i == p:
            return False
        q = i

        # 🔑 MUST have room for third increasing segment
        if i >= n - 1:
            return False

        # Phase 3: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1
