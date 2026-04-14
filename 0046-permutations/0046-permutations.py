class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(path, used):
            # If permutation is complete
            if len(path) == len(nums):
                result.append(path[:])  # make a copy
                return
            
            # Try every number
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # Choose
                path.append(nums[i])
                used[i] = True
                
                # Explore
                backtrack(path, used)
                
                # Undo (backtrack)
                path.pop()
                used[i] = False
        
        # used array to track picked elements
        used = [False] * len(nums)
        backtrack([], used)
        
        return result