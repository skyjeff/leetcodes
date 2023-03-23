#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        def back(begin, total, path):
            if len(path) == k and total == 0:
                res.append(path)
            for i in range(begin, 10):
                if total - i >= 0:
                    back(i+1, total - i, path + [i])

        back(1, n, [])
        return res
# @lc code=end
x= Solution().combinationSum3(9,45)
print(x)

