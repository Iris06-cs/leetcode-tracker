class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force
        # for i, val in enumerate(nums):
        #     diff = target - val
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == diff:
        #             return [i, j]
        # return []

        # fast solution
        tracker = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in tracker:
                return [tracker[diff], i]
            tracker[val] = i


































#         input:array of int and a int number
#         output: array of index
#         get the diff of element and the target, and see if the diff is also in the array
        # if so return the two index otherwise return []
        # try to complete in better time complexity than O(n^2)
#         O(n^2)
#         res=[]
#         for i,num in enumerate(nums):
#             diff=target-num
#             rest_nums=nums[i+1:len(nums)]
       
#             for j,num_rest in enumerate(rest_nums):
#                 if diff==num_rest:
#                     res.append(i)
#                     res.append(i+j+1)
#                     return res
                
#         return res
        # better solution


        # tracker={}
        # for idx, num in enumerate(nums):
        #     diff=target-num
        #     if diff in tracker:
        #         return [tracker[diff],idx]
        #     tracker[num]=idx
             
        # return []
                

                
            

        