class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
#         new_str = ""
#         i = 0
#         j = 0
# #         add char from each word string alternately till one of the string reached the end
#          # add rest chars to the end 
#         while i < len(word1) and j < len(word2):
#             new_str += word1[i]
#             new_str += word2[j]
#             i += 1
#             j += 1
#         if i == len(word1):
#             new_str += word2[j:]
#         else:
#             new_str += word1[i:]
#         return new_str
        merged_parts = [char for pair in zip(word1, word2) for char in pair] #zip will stop merge two string till the shorter length
    
        remainder = word1[len(merged_parts)//2:] + word2[len(merged_parts)//2:] # length of merged string should be twice of the shorter one
        return ''.join(merged_parts) + remainder
            