class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = []
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                new.append(num)
        
        new.extend([0] * zeros)
        
        for i in range(len(nums)):
            nums[i] = new[i]

