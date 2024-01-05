class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        splited_path=path.split("/")
        
        for sub_str in splited_path:
            if sub_str=="..":
                if stack:
                    stack.pop()
            elif sub_str=="." or not sub_str:
                continue
            else:
                stack.append(sub_str)
        res="/"+"/".join(stack)
        return res
        