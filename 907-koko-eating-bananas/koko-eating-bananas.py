class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get the max pile number, and the range of k would be 1-max
        # start from the middle, if by that speed will finish > h hours, move pointers to right of middle, otherwise move left
        # track the k value can finish < h hours, continue to try till curr_hour>h
        
        l = 1
        r = max(piles)
        while l < r:
            mid =(l+r)//2
            curr_hour = 0
            for num in piles:
                if num <= mid:
                    curr_hour += 1
                else:
                    curr_hour += ceil(num / mid)
                
            if curr_hour > h:
                l = mid + 1
            else:
                r = mid
        return r
                
                

        