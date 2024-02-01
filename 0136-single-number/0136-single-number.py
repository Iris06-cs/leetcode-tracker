class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # must done in linear runtime
        # spacial case arr length 1, return the element directly
        # use hashmap to keep track of num frequency O(n)
        # find the num with only 1 count
        
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 0
            freqs[num] += 1

        
        for num in nums:
            if freqs[num] == 1:
                return num

        