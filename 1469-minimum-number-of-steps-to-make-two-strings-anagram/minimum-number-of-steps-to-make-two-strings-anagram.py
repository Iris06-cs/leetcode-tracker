class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter_s = Counter(s)
        counter_t = Counter(t)
        change = 0
        for char in set(counter_s.keys()).union(counter_t.keys()):
            change += abs(counter_s[char] - counter_t[char])
        
        # double-counting
        # need to divide by 2 to get the actual number of changes needed
        return change // 2