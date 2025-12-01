class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        # A mountain must have at least 3 elements
        if n < 3:
            return False
        
        i = 0
        
        # Climb uphill
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # Peak cannot be first or last
        if i == 0 or i == n - 1:
            return False
        
        # Walk downhill
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        # If we reached the end, it's a valid mountain
        return i == n - 1
