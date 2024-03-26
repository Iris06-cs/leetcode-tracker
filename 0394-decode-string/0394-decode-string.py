class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        stack =[]
   
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                sub_str = ""
                while stack[-1] !="[":
                    sub_str += stack.pop()
                # pop off "["
                stack.pop()
                times = ""
                while len(stack) and stack[-1].isdigit():
                    times += stack.pop()
                stack.append(sub_str * int(times[::-1]))
                    
        res = "".join([sub_str[::-1] for sub_str in stack])  
        return res
                
        
      
        