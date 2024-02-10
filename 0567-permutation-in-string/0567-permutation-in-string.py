class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # to check if s2 contains sub-stirng with s1's length and same number of same letter(order doesn't matter?)
#         letter_counts = {}
#         for letter in s1:
#             if letter not in letter_counts:
#                 letter_counts[letter] = 0
#             letter_counts[letter] += 1
            
#         n = len(s1)
#         # brute force
        
#         for i in range(len(s2) - n + 1):
#             j = i + n - 1
#             sub_str = s2[i:j + 1]
#             temp = {key:value for key,value in letter_counts.items()}
#             for char in sub_str:
#                 if char not in temp:
#                     break
#                 else:
#                     temp[char] -= 1
                    
#             if all(val == 0 for val in temp.values()):
#                 return True
#         return False
    # sliding window, avoid recalculating the count for every new window
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26 # representing the number of letter from a to z
        s2_count = [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (s1_count[i] == s2_count[i])
        
        for i in range(len(s1), len(s2)):
            if matches == 26:  # All character counts match
                return True
            
            index = ord(s2[i]) - ord('a')
            s2_count[index] += 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] - 1 == s1_count[index]:
                matches -= 1
            
            index = ord(s2[i-len(s1)]) - ord('a')
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] + 1 == s1_count[index]:
                matches -= 1
        
        return matches == 26
        
    
            