#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        x, y = 0, len(matrix[0])-1
        
        
        
# @lc code=end

x = Solution().searchMatrix(
[[1]],
2)
print(x)