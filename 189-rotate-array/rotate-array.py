class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if k same as nums length=> no need to rotate
        # k%length=> steps need to rotate
        steps = k % len(nums)
        # for i in range(steps):#exceeded time limit
        #     prev = nums[-1]
        #     for j in range(len(nums)):
        #         curr = nums[j]
        #         nums[j] = prev
        #         prev = curr
        n = len(nums)
        # temp = nums[n-steps:]+nums[:n-steps] #extra space
        # # print(temp)
        # for i in range(len(nums)):
        #     nums[i] = temp[i]
        
        nums[:] = nums[n-steps:]+nums[:n-steps]