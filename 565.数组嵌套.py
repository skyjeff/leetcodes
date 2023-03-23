#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#

# @lc code=start
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        res = 1
        for i in range(n):
            j = i
            cur = nums[j]
            next = nums[cur]
            len_ = 1
            while dp[j] == -1 and cur != next:
                dp[j] = len_
                j = cur
                cur = nums[j]
                next = nums[cur]
                len_ += 1
            res = max(res, len_-1)
        return res
# @lc code=end
Solution().arrayNesting([5,4,0,3,1,6,2])

