class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening = res = 0
        for char in s:
            if char == "(":
                opening += 1
            else:
                if char == ")":
                    if opening:
                        opening -= 1
                    else:
                        res += 1
        return res + opening
                    
        