class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        for i, word in enumerate(s_list):
            reversed_word =  word[::-1]
            s_list[i] = reversed_word
        return " ".join(s_list)
        