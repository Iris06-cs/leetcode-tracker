class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        columns, rows=len(matrix[0]), len(matrix)
        result=[]
#         set boundres
        up = left = 0
        right = columns - 1
        down = rows - 1
        
        while len(result) < rows * columns:
            # left to right.
            for col in range(left, right+1):
                result.append(matrix[up][col])

            # downwards.
            for row in range(up + 1, down+1):
                result.append(matrix[row][right])

            # Make sure on a different row.
            if up != down:
                # right to left.(reverse loop)
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure on a different column.
            if left != right:
                # upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
            
        
        
        