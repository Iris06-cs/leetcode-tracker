class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_idxes = set()
        stack = []
        for idx, char in enumerate(s):
            # ignore letters,push open parentheses to stack,pop close parentheses when stack not empty
            # push index of close parenthese when stack is empty
            if char not in "()":
                continue
            elif char == "(":
                stack.append(idx)
            elif char == ")" and len(stack) == 0:
                remove_idxes.add(idx)
            else:
                stack.pop()
        # when stack is not empty, add the indexes to be removed
        remove_idxes = remove_idxes.union(set(stack))
        res = []
        for idx, char in enumerate(s):
            if idx not in remove_idxes:
                res.append(char)
        return "".join(res)
        