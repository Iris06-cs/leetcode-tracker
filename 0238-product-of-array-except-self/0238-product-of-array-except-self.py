class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         brute force, double loop O(n^2) time limit exceeded
        # answer=[]
        # for i in range(len(nums)):
        #     num=1
        #     for j in range(len(nums)):
        #         if i != j:
        #             num*=nums[j]
        #     answer.append(num)
        # return answer
        
# must be O(n) time and no division operation
        # product_before=[]
        # product_after=[]
        # answer=[]
        # for num in nums:
        #     if not len(product_before):
        #         product_before.append(num)
        #     else:
        #         product_before.append(num * product_before[-1])
        # for i in range(len(nums)-1,-1,-1):
        #     num=nums[i]
        #     if not len(product_after):
        #         product_after.append(num)
        #     else:
        #         product_after.append(num * product_after[-1])
        # product_after.reverse()       
        # for i in range(len(nums)):
        #     if i == 0:
        #         answer.append(product_after[i+1])
        #     elif i == len(nums)-1:
        #         answer.append(product_before[i-1])
        #     else:
        #         answer.append(product_before[i-1] * product_after[i+1])
        # return answer
        
#         O(1) space?
        answer=[]
        pref=1
        for i in range(len(nums)):
            pref=pref * nums[i]
            answer.append(pref)
        # print(answer)
        
        post=nums[-1]
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                answer[j]=answer[j-1]
            elif j == 0:
                answer[j]=post
            else:
                answer[j]=post * answer[j-1]
                post *= nums[j]
        return answer
                
            

        
        