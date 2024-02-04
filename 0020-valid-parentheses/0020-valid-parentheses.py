class Solution:
    def isValid(self, s: str) -> bool:
#         add opening parentheses to stack then pop off when having matching closing parenthese
        # stack=[]
        # openings=["(","[","{"]
        # closings={")":"(","}":"{","]":"["}
        # for char in s:
        #     if char in openings:
        #         stack.append(char)
        #     else:
        #         if stack and closings[char]==stack[-1]:
        #             stack.pop()
        #         else:
        #             return False
        # return True if not stack else False
        
        stack = []
        for char in s:
            # 压栈
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            else:
                # check if stack is empty
                if not stack: # empty stack, try to push in closing parentheses
                    return False
                # check if the top of stack will match
                if char == "]" and stack[-1] != "[" or char == "}" and stack[-1] != "{" or char == ")" and stack[-1] != "(":
                    return False
                stack.pop()
                # whether stack is empty
        return not stack
        
        
        
        