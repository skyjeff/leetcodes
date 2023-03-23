#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = [0 for i in range(len(triangle[-1]) + 1)]

        for i in range(len(triangle)-1,-1,-1):
            for j in range(len(triangle[i])-1,-1,-1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        print(dp[0])
        
# @lc code=end
Solution().minimumTotal( [[2],[3,4],[6,5,7],[4,1,8,3]])
