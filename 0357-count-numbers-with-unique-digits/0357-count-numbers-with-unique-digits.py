class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
#         when n> 9 digits number, no more numbers with unique digits
#         1digit choose 1 out of 9 cannot start with 0
          # 2digits choose 9* 1 out of 9...
#     n=1 0-9
#     n=2 100 0-99
#.    n=3

        if n==0:
            return 1
        res=10
        choices=9
        digit_sum=9
        while n>1 and choices>0:
            digit_sum=digit_sum * choices
            res+=digit_sum
            choices-=1
            n-=1    
        return res
        
            
            
        
    