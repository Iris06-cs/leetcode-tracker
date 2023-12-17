class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
#         change to binary format
        return sorted(arr,key=lambda x:(bin(x).count("1"),x))
        
        
        