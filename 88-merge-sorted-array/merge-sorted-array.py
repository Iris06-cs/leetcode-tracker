class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge nums2 into nums1
        # brute force replace elements from m+1 by elements in nums2; then sort nums1
        for i in range(m,m+n):
            nums1[i] = nums2[i - m]
        
        nums1.sort()