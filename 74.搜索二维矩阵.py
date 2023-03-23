#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r-l)//2
            mid_x, mid_y = mid // n, mid % n

            if matrix[mid_x][mid_y] < target:
                l = mid + 1
            elif matrix[mid_x][mid_y] > target:
                r = mid - 1
            else:
                return True
        return False

        
# @lc code=end
x= Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],
1)
print(x)

