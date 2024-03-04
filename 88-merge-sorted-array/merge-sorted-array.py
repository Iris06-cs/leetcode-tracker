class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # merge nums2 into nums1
        # brute force replace elements from m+1 by elements in nums2; then sort nums1
        # for i in range(m,m+n):
        #     nums1[i] = nums2[i - m]
        # nums1.sort()  O((n+m)log(n+m))
        
        # optimized solution O(n+m)
        nums1_copy = nums1[:m]
        p1 = p2 = 0
        i = 0
        while i < m+n:
            # Check if p2 is out of bounds, meaning all elements from nums2 are already inserted
            if p2 >= n:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            # Check if p1 is out of bounds OR nums1_copy[p1] is greater than nums2[p2]
            elif p1 >= m or (p2 < n and nums1_copy[p1] > nums2[p2]):
                nums1[i] = nums2[p2]
                p2 += 1
            else:
                nums1[i] = nums1_copy[p1]
                p1 += 1
            i += 1