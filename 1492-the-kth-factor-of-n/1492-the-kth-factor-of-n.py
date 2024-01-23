class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # brute force
        # loop each number from 1 to n to find all factors
        factors = []
        for num in range(1,n+1):
            if n % num == 0:
                factors.append(num)
                
        if len(factors) < k:
            return -1
        return factors[k-1]
        
        