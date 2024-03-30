class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # keep track of count of each number in nums
        # the max count will be the number of rows the result has
        hash_map = Counter(nums)
        
        row_num = max(hash_map.values())
        res = [[] for _ in range(row_num)]
        
        for num in nums:
            while hash_map[num] > 0:
                # count - 1 will be the last row idx has the number
                res[hash_map[num] - 1].append(num)
                hash_map[num] -= 1
        return res
            
        
