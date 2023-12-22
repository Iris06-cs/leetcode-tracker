class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         char_set = set()
#         l = 0
#         max_length= 0

#         for r in range(len(s)):
#             while s[r] in char_set:
#                 char_set.remove(s[l])
#                 l += 1
#             char_set.add(s[r])
#             max_length = max(max_length, r - l + 1)
#         return max_length
        if len(s)<=1:
            return len(s)
        char_set=set()
        left,right=0,0
        max_length=1
        while right<len(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[right])
            max_length=max(max_length,right-left+1)
            right+=1
            
        return max_length
        
            