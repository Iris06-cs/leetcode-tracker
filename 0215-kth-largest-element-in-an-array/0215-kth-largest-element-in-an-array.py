class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force sorting
        sorted_nums = sorted(nums, reverse = True)
        for i, num in enumerate(sorted_nums):
            if i == k - 1:
                return num
        