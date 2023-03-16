#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
import sys
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n = len(nums)
        nums.sort()
        min_diff = sys.maxsize
        min_total = sys.maxsize
        for i in range(n):
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return target
                if abs(total - target) < min_diff:
                    min_diff = abs(total - target)
                    min_total = total
        return min_total
                
# @lc code=end
Solution().threeSumClosest([-1,2,1,-4],
1)

