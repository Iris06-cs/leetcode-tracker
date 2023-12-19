class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
#         track the freq
#         cal freq diff
        freqs=Counter(word1)
        for char in word2:
            if char in freqs.keys():
                freqs[char]-=1
            else:
                freqs[char]=-1
        max_diff=max(abs(freq) for freq in freqs.values() )
        return max_diff<=3
        
                