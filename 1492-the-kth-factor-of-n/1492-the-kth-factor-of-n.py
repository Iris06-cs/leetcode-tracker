class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # brute force
        # loop each number from 1 to n to find all factors
#         factors = []
#         for num in range(1,n+1)://O(n)
#             if n % num == 0:
#                 factors.append(num)
                
#         if len(factors) < k:
#             return -1
#         return factors[k-1]

        # less than O(n)
        # smallest factor is 1 largest factor is n itself
        # loop when k > 0, if find a factor minus k till k=0
        num = 1
        factor = -1
        while k > 0 and num <= n:
            if n % num == 0:
                if k == 1:
                    factor = num
                k -= 1
            num += 1
        return factor
        
        
                
        
        