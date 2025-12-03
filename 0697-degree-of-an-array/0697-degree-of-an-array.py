class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}
        last = {}
        
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            count[x] = count.get(x, 0) + 1
        
        degree = max(count.values())
        ans = float('inf')
        
        for x in count:
            if count[x] == degree:
                ans = min(ans, last[x] - first[x] + 1)
        
        return ans