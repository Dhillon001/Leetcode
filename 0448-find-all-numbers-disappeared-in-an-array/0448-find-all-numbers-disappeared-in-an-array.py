class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # Step 1: Mark visited
        for x in nums:
            index = abs(x) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Step 2: Collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result