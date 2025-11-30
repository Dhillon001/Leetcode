class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter
        freq = Counter(nums)
        
        # If any number appears 3 or more times -> impossible
        for count in freq.values():
            if count > 2:
                return False
        
        return True
