class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = curr_cost = res = 0
        for i in range(len(s)):
            curr_cost += abs(ord(s[i])-ord(t[i]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left])-ord(t[left]))
                left += 1
            res = max(res, i - left + 1)
        return res
        