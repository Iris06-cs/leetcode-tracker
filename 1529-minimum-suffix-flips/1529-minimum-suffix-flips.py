class Solution:
    def minFlips(self, target: str) -> int:
        n=0
        flag="0"
        for num in target:
            if flag !=num:
                flag=num
                n+=1
         
        return n
        