from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        
        ugly = [1] * n          # stores the sequence
        idx = [0] * k           # pointers for each prime
        values = primes[:]      # current multiples
        
        for i in range(1, n):
            next_val = min(values)
            ugly[i] = next_val
            
            for j in range(k):
                if values[j] == next_val:
                    idx[j] += 1
                    values[j] = primes[j] * ugly[idx[j]]
        
        return ugly[-1]