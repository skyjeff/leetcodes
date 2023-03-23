#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = list(triangle[-1])
        for i in range(n-2,-1,-1):
            for j in range(0, len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
# @lc code=end
x = Solution().minimumTotal([[-10]])
print(x)

