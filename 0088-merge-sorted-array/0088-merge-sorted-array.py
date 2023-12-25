class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        m_elements=nums1[:m]
        idx1,idx2=0,0
        for i in range(n+m):
            if idx2>=n or (idx1<m and m_elements[idx1]<=nums2[idx2]):
                nums1[i]=m_elements[idx1]
                idx1+=1
            else:
                nums1[i]=nums2[idx2]
                idx2+=1
        