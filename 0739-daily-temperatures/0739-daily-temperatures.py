class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         brute force 2 loop O(n^2)
#         n = len(temperatures)
#         ans = [0] * n
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if temperatures[j] > temperatures[i]:
#                     ans[i] = j - i
#                     break
                
#         return ans
        
        # use stack
        n = len(temperatures)
        ans = [0] * n
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
        