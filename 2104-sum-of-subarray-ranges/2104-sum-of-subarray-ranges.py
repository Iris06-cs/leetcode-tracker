# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:
#         if len(nums)==1:
#             return 0
#         sum=0
#         sub_arrs=[]
#         for start in range(len(nums)):
#             for end in range(start+1,len(nums)+1):
#                 sub_arr=nums[start:end]
#                 sub_arrs.append(sub_arr)
#         print(sub_arrs)
#         for sub_arr in sub_arrs:
#             sum+=(max(sub_arr)-min(sub_arr))
#         return sum

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        total = 0

        for i in range(n):
            min_val, max_val = nums[i], nums[i]
            for j in range(i, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                total += max_val - min_val

        return total

        