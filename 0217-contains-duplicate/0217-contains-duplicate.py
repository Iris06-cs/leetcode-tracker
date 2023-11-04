class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         numCount={}
#         for num in nums:
#             if not num in numCount.keys():
#                 numCount[num]=0
#             numCount[num]+=1
#         for count in numCount.values():
#             if count!=1:
#                 return True
            
#         return False

# use set
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
        return len(nums) != len(set(nums))
        