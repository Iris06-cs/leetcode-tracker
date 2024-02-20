class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums[0]<nums[len-1]=> in sorted order already
        l = 0
        r = len(nums) - 1

        
        while l <= r:
            mid  = (l + r) // 2

            if nums[mid] == target:
                return mid
            # left half is sorted
            elif nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]: # target in the left harf range
                    r = mid - 1
                else:
                    l = mid + 1
                           
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
            