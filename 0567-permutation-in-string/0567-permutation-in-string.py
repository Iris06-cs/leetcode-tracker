class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # to check if s2 contains sub-stirng with s1's length and same number of same letter(order doesn't matter?)
        letter_counts = {}
        for letter in s1:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1
            
        n = len(s1)
        # sliding window
        
        for i in range(len(s2) - n + 1):
            j = i + n - 1
            sub_str = s2[i:j + 1]
            temp = {key:value for key,value in letter_counts.items()}
            for char in sub_str:
                if char not in temp:
                    break
                else:
                    temp[char] -= 1
                    
            if all(val == 0 for val in temp.values()):
                return True
        return False
            