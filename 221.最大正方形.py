#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0 for i in range(n)]
        res = 0
        for i in range(m):
            for j in range(n):
                tmp = dp[j]
                if i == 0 or j == 0:
                    dp[j] = int(matrix[i][j])    
                elif matrix[i][j] == '0':
                    dp[j] = 0
                elif matrix[i][j] == '1':
                    dp[j] = min(dp[j], dp[j-1], topleft) + 1
                res = max(res, dp[j])
                topleft = tmp
        return res*res

# @lc code=end

input = [["1","1","1","0","0"],
         ["1","1","1","1","1"],
         ["1","1","1","1","1"],
         ["1","1","1","1","1"]]
Solution().maximalSquare(input)
