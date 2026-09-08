class Solution:
    def subsets(self, nums):
        res = []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Don't include nums[i]
            subset.pop()
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res