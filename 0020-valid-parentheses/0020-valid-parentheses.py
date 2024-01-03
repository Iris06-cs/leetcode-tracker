class Solution:
    def isValid(self, s: str) -> bool:
#         add opening parentheses to stack then pop off when having matching closing parenthese
        stack=[]
        openings=["(","[","{"]
        closings={")":"(","}":"{","]":"["}
        for char in s:
            if char in openings:
                stack.append(char)
            else:
                if stack and closings[char]==stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        
        
        