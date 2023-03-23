#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = False
        col_flag = False
        m, n = len(matrix), len(matrix[0])
        
        # 不能在下面一起判断，因为假如某一行有两个0，那么在第一个0置col为0后，那么后一个0会认为col本身就是0
        # 判断row是否有0
        for i in range(n):
            if matrix[0][i] == 0:
                row_flag = True
        
        # 判断col是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                col_flag = True
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if row_flag:
            for i in range(n):
                matrix[0][i] = 0
                
        if col_flag:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix 
    
# @lc code=end
Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])
