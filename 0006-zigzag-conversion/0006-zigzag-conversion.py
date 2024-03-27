class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # special case
        if numRows == 1:
            return s
        length = len(s)
        numCols = ceil(length / (numRows - 2 + numRows)) * (numRows - 1)
        # empty matrix
        matrix = [[" "] * numCols for _ in range(numRows)]
        
        curr_row = curr_col = 0
        curr_idx = 0
        
        while curr_idx < length:
            # move down the matrix
            while curr_row < numRows and curr_idx < length:
                matrix[curr_row][curr_col] = s[curr_idx]
                curr_row += 1
                curr_idx += 1
               
            # move diagonal up
            curr_row -= 2
            curr_col += 1
            while curr_row > 0 and curr_col < numCols and curr_idx < length:
                matrix[curr_row][curr_col] = s[curr_idx]
                curr_row -= 1
                curr_col += 1
                curr_idx += 1
                
        res = ""
        for row in matrix:
            for cell in row:
                if cell != " ":
                    res += cell
        return res
            
        
        