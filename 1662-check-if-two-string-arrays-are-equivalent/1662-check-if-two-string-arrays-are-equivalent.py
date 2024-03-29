class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1) == "".join(word2)
        word1_idx = sub1_idx = 0
        word2_idx = sub2_idx = 0
        
        while word1_idx < len(word1) and word2_idx < len(word2):
            curr_char1 = word1[word1_idx][sub1_idx]
            curr_char2 = word2[word2_idx][sub2_idx]
            if curr_char1 != curr_char2:
                return False
            sub1_idx += 1
            sub2_idx += 1
            
            if sub1_idx == len(word1[word1_idx]):
                sub1_idx = 0
                word1_idx += 1
            if sub2_idx == len(word2[word2_idx]):
                sub2_idx = 0
                word2_idx += 1

        return word1_idx == len(word1) and word2_idx == len(word2)
            

        
        