class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
#         track the freq
#         cal freq diff
        # freqs=Counter(word1)
        # for char in word2:
        #     if char in freqs.keys():
        #         freqs[char]-=1
        #     else:
        #         freqs[char]=-1
        # max_diff=max(abs(freq) for freq in freqs.values() )
        # return max_diff<=3
        
        freqs1=Counter(word1)
        freqs2=Counter(word2)
        for char,freq in freqs1.items():
            if char not in freqs2.keys() and freq>3:
                return False
            if char in freqs2.keys() and abs(freq-freqs2[char])>3:
                return False
            
        for char,freq in freqs2.items():
            if char not in freqs1.keys() and freq>3:
                return False
            if char in freqs1.keys() and abs(freq-freqs1[char])>3:
                return False
        return True
                
            
            
        
                