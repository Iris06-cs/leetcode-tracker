                
class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the pivot
        pivot = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i
                break

        if pivot == 0:  # If no pivot is found, it's the last permutation
            nums.reverse()
            return

        # Find the number just larger than the pivot in the remaining part of the array
        for i in range(len(nums) - 1, pivot - 1, -1):
            if nums[i] > nums[pivot - 1]:
                nums[i], nums[pivot - 1] = nums[pivot - 1], nums[i]  # Swap
                break

        # Reverse the part of the array after the pivot
        nums[pivot:] = reversed(nums[pivot:])

                
            
                    
                
            
        