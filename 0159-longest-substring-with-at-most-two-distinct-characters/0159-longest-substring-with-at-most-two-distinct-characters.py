class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         two pointer
#         start both left and right and 0
#         move the right to next position, and if char changed, increase count of chars
#         if char count is greater than 3, then move the right to next, and reset count and move the left to the same place where the right place, and continue the same
        length=len(s)
        if length<3:
            return length

        left,right=0,0
        max_length=0
        char_tracker={}
        while right<length:
            curr_char=s[left]
            next_char=s[right]
            char_tracker[next_char]=right
            right+=1
  
            if len(char_tracker)==3:
                delete_idx=min(char_tracker.values())
                del char_tracker[s[delete_idx]]
                left=delete_idx+1
            max_length=max(max_length,right-left)

            
                
        return max_length
                
                
            
            
                
            
                
        