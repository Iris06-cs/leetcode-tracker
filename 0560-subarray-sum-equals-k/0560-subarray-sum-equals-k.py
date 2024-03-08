class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        res = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         sub_total = sum(nums[i:j+1])
        #         if sub_total == k:
        #             res += 1
        # return res
        
        # optimized
#         if len(nums) <= 1:
#             return res if nums[0] != k else 1
#         start = end = 0
#         sub_total = 0
#         while end < len(nums):
#             sub_total += nums[end]
#             print(sub_total,start,end)
#             while sub_total > k and start <= end:
#                 sub_total -= nums[start]
#                 start += 1
            
#             if sub_total == k:
#                 res += 1
            
#             end += 1
#         return res  # not working for negtive value
        res = 0
        sub_total = 0
        hashmap = {0:1}
        for num in nums:
            sub_total += num
            if sub_total - k in hashmap:
                res += hashmap[sub_total - k]
            if sub_total in hashmap:
                hashmap[sub_total] += 1
            else:
                hashmap[sub_total] = 1
        return res
        
        