class Solution:
    def findMin(self, nums: List[int]) -> int:
        # must log n time; cannot sort or brute force loop
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[l]:
                return nums[l]
        while nums[l] > nums[r]:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
        
                
            
            
        
        