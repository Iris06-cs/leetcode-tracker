class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
#         # two pointers start from 0
#         # if str[l:r+1] in forbidden then substring start from l will not meet requirement; set r equal to l;l+1
#         # otherwise move r to right by 1 
# time limit exceeded
        l = r = 0
        res = 0
        forbidden_set = set(forbidden)
        # while r < len(word):
        #     is_valid = True
        #     for not_valid_str in forbidden_set:  
        #         if not_valid_str in word[l:r+1]:
        #             is_valid = False
        #             break
        #     if is_valid:
        #         res = max(res, len(word[l:r+1]))  
        #         r += 1
        #     else:
        #         r = l
        #         l += 1
        # return res  
        while r < len(word):
            for index in range(max(0,r-9), r+1): # max length of forbidden word is 10
                if word[index:r+1] in forbidden_set:
                    l = max(l,index+1)
            res = max(res, r - l +1)
            r += 1
        return res 

    