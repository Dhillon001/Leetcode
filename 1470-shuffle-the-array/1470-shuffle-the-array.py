class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])      # xi
            res.append(nums[i + n])  # yi
        return res
