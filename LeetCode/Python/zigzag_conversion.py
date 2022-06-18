def cal_matrix_dim(s, numRows):
    
    # number of characters needed per zigzag
    num_chars = numRows
    # extra characters
    if numRows > 2:
        num_chars = num_chars + (numRows - 2)
        
    # print('num_chars:', num_chars)
    
    # number of columns needed per zigzag
    # one for the rows, extra ones for the extra characters
    num_cols = 1 + (num_chars - numRows)
    
    # print('num_cols:', num_cols)
    
    # number of column groups for the entire word
    num_col_groups = len(s) / float(num_chars) # weird why it doesn't keep the decimal
    
    # print('num_col_groups:', num_col_groups)
    
    final_col_dim = int(num_col_groups) * num_cols
    
    # print('final_col_dim:', final_col_dim)
    
    # if it has a decimal - extra column for the hanging characters
    if num_col_groups - int(num_col_groups) != 0:
        final_col_dim = final_col_dim + 1
        # print('it has a decimal so adding one:', final_col_dim)
        
    # print('Final dimensions:', numRows, final_col_dim)
        
    return (numRows, final_col_dim)
    
    
def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    
    dim_row, dim_col = cal_matrix_dim(s, numRows)
    
    # creates 2-d array
    matrix = [[' ' for i in range(dim_col)] for j in range(dim_row)]
    
    row = 0
    col = 0
    direction = 'down'
    
    for char in s:
        
        # print('Row:',row,',Col:',col,'Char:',char)
        # place character in matrix
        matrix[row][col] = char
        
        # increase the indexes
        if direction == 'down': # if down, the column index stays the same, but row increases
            row = row + 1
        elif direction == 'up': # if up, column index increases, row decreases by 1
            col = col + 1
            row = row - 1
        else:
            print('something went wrong')
            
        # check if direction changes
        if row == (numRows-1):
            direction = 'up'
        elif row == 0:
            direction = 'down'
            
        # for r in range(len(matrix)):
        #     print(matrix[r])

    final_str = ''
    for r in range(len(matrix)):
        for c in range(len(matrix[row])):
            if matrix[r][c] != ' ':
                final_str += matrix[r][c]
    
    return final_str
        
def main():

    s = "PAYPALISHIRING"
    numRows = 4

    output = convert(s, numRows)

    print(output)
                
main()
                
            
# class Solution(object):
    
#     def cal_matrix_dim(self, s, numRows):
        
#         # number of characters needed per zigzag
#         num_chars = numRows
#         # extra characters
#         if numRows > 2:
#             num_chars = num_chars + (numRows - 2)
            
#         # print('num_chars:', num_chars)
        
#         # number of columns needed per zigzag
#         # one for the rows, extra ones for the extra characters
#         num_cols = 1 + (num_chars - numRows)
        
#         # print('num_cols:', num_cols)
        
#         # number of column groups for the entire word
#         num_col_groups = len(s) / float(num_chars) # weird why it doesn't keep the decimal
        
#         # print('num_col_groups:', num_col_groups)
        
#         final_col_dim = int(num_col_groups) * num_cols
        
#         # print('final_col_dim:', final_col_dim)
        
#         # if it has a decimal - extra column for the hanging characters
#         if num_col_groups - int(num_col_groups) != 0:
#             final_col_dim = final_col_dim + 1
#             # print('it has a decimal so adding one:', final_col_dim)
            
#         # print('Final dimensions:', numRows, final_col_dim)
            
#         return (numRows, final_col_dim)
        
        
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
        
        
#         dim_row, dim_col = self.cal_matrix_dim(s, numRows)
#         print('String:',s,'Dimensions:', dim_row, dim_col)
    
#         # creates 2-d array
#         matrix = [[' ' for i in range(dim_col)] for j in range(dim_row)]

#         row = 0
#         col = 0
#         direction = 'down'

#         for char in s:

#             print('Row:',row,',Col:',col,'Char:',char)
#             # place character in matrix
#             matrix[row][col] = char

#             # increase the indexes
#             if direction == 'down': # if down, the column index stays the same, but row increases
#                 row = row + 1
#             elif direction == 'up': # if up, column index increases, row decreases by 1
#                 col = col + 1
#                 row = row - 1

#             # for r in range(len(matrix)):
#             #     print(matrix[r])
            
#             # check if direction changes
#             if row == (numRows-1):
#                 direction = 'up'
#             elif row == 0:
#                 direction = 'down'

#         final_str = ''
#         for i in range(dim_row):
#             for j in range(dim_col):
#                 if matrix[i][j] != ' ':
#                     final_str += matrix[i][j]
                    
#         return final_str        
        
        
        