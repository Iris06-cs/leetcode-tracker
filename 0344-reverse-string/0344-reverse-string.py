class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # start = 0
        # end = len(s) -1
        # while start <= end:
        #     temp = s[start]
        #     s[start] = s[end]
        #     s[end] = temp
        #     start += 1
        #     end -= 1
        
        start, end = 0, len(s) - 1
        while start <= end:
            s[start], s[end] = s[end], s[start]  # Tuple unpacking for swap
            start, end = start + 1, end - 1

        