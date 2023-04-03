#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l= 0
        sum = 1
        res = 0
        for j in range(n):
            sum *= nums[j]
            while sum >= k and l <= j:
                sum //= nums[l]
                l+=1
            res += j - l + 1
        return res
# @lc code=end
Solution().numSubarrayProductLessThanK([10,5,2,6],
100)