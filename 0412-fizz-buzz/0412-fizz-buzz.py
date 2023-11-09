# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         answer=[]
# #         loop from 1 to n
#         for i in range(1,n+1):
#             if i % 3 == 0 and i % 5 == 0:
#                 answer.append("FizzBuzz")
#             elif i % 3 == 0 and i % 5 != 0:
#                 answer.append("Fizz")
#             elif i % 5 == 0 and i % 3 != 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(i))
#         return answer

class Solution:
    def fizzBuzz(self,n: int) -> List[str]:
        answer=[]
        for i in range(1, n+1):
            ans=""
            if i % 3 == 0:
                ans+="Fizz"
            if i % 5 == 0:
                ans+="Buzz"
            if not ans:
                ans=str(i)
            answer.append(ans)
        return answer