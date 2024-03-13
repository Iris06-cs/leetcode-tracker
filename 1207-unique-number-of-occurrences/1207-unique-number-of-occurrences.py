class Solution:
    # def uniqueOccurrences(self, arr: List[int]) -> bool:
    #     hashmap = {}
    #     for num in arr:
    #         if num not in hashmap:
    #             hashmap[num] = 0
    #         hashmap[num] += 1
    #     freqs = set(hashmap.values())
    #     return len(freqs) == len(hashmap.values())
    # use counter collection
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr)
        freqs = occurrences.values()
        return len(set(freqs)) == len(freqs)
        
        