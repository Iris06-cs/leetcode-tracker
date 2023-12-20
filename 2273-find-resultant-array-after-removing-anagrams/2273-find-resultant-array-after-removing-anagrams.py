class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # def is_anagrams(str1:List[str],str2:List[str]) -> bool:
        #     if len(str1) != len(str2):
        #         return False
        #     char_counter=Counter(str1)
        #     for char in str2:
        #         if char in char_counter.keys():
        #             char_counter[char]-=1
        #         else:
        #             char_counter[char]=-1
        #     for count in char_counter.values():
        #         if count != 0:
        #             return False
        #     return True
        def is_anagrams(str1: str, str2: str) -> bool:
            return sorted(str1) == sorted(str2)
        
        res=[words[0]]
        for i in range(1,len(words)):
            if not is_anagrams(res[-1],words[i]):
                res.append(words[i])
        return res
                
        
        