class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCount={}
        for num in nums:
            if not num in numCount.keys():
                numCount[num]=0
            numCount[num]+=1
        for count in numCount.values():
            if count!=1:
                return True
            
        return False
        