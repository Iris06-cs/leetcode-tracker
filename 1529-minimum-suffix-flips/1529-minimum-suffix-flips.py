class Solution:
    def minFlips(self, target: str) -> int:
        n=0
        flag="0"
        for num in target:
            if flag !=num:
                if num=="0":
                    flag="0"
                else:
                    flag="1"
                n+=1
         
        return n
        