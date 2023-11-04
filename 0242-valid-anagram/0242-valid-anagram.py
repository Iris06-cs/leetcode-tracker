class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# dict to track appearance of each char in first str
# loop through 2nd str, each appearance of char minus 1 in the dict
# if all value in dict is 0 at the end-true
        tracker={}
        for char in s:
            if not char in tracker.keys():
                tracker[char]=0
            tracker[char]+=1
        for char in t:
            if not char in tracker.keys():
                return False
            tracker[char]-=1
        for val in tracker.values():
            if val != 0:
                return False
            
        return True
    
    
        