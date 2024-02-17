class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # change matrix to 1-d array
        row = len(matrix)
        if row == 0:
            return Fasle
        col = len(matrix[0])
        
        l = 0
        r = row * col - 1
        while l <= r:
            mid = (r + l) // 2
            mid_num = matrix[mid // col][mid % col]
            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        
#         top = 0
#         down = len(matrix) - 1
#         while top <= down:
#             mid_row = (top + down) // 2
#             mid_row_l = 0
#             mid_row_r = len(matrix[mid_row]) - 1
            
#             if matrix[mid_row][mid_row_r]<target :
#                 # move down
#                 top = mid_row + 1
#             elif matrix[mid_row][mid_row_l]>target:
#                 # move up
#                 down = mid_row - 1
#             else:
#                 while mid_row_l <= mid_row_r:
#                     mid_row_mid_col = (mid_row_l + mid_row_r) // 2
#                     if matrix[mid_row][mid_row_mid_col] == target:
#                         return True
#                     elif matrix[mid_row][mid_row_mid_col] > target:
#                         mid_row_r = mid_row_mid_col - 1
#                     else:
#                         mid_row_l = mid_row_mid_col + 1
#                 return False
            
#         return False
  
        