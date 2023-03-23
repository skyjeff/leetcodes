#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List
import sys


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        index = False
        left, right = newInterval
        for li, ri in intervals:
            if ri < left:
                res.append([li,ri])
            elif li > right:
                if not index:
                    res.append([left, right])
                    index = True
                res.append([li, ri])
            else:
                left = min(left, li, newInterval[0])
                right = max(right, ri, newInterval[1])
        if not index:
            res.append([left, right])
        return res
                


# @lc code=end
Solution().insert([[1,3],[6,9]],
[2,5])

