class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs=0
        
        for i, num_i in enumerate(nums):
            for j in range(i+1,len(nums)):
                num_j=nums[j]
                if num_i+num_j<target:
                    pairs+=1
        return pairs
        