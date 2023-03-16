#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        start = 0
        end = 1
        while end < n:
            max_pos = 0
            for i in range(start, end):
                # print(i)
                max_pos = max(max_pos, i + nums[i])
            start = end
            end = max_pos + 1
            res += 1
        return res

# @lc code=end

x = Solution().jump([2,3,0,1,4,1])
print(x)