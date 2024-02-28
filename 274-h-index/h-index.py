class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations,reverse = True)
        # len(citations) => number of papers
        # citations[i]=> each paper's citation times
        # h-index==> at least h papers have been citated at least h times
        h = 0
        for idx, count in enumerate(sorted_citations):
            if count >= idx + 1:
                h = idx + 1
            else:
                break
        return h
        
        
        