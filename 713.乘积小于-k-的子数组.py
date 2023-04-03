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
        l = 0
        res = 0
        sum = 1
        for i in range(n):
            if nums[i] < k:
                res += 1
            sum *= nums[i]
            if sum < k:
                res += 1
            while sum >= k and l <= i:
                sum //= nums[l]
                l+=1
            if sum < k:
                res += 1
        return res-1
            
# @lc code=end
Solution().numSubarrayProductLessThanK([1,5,20,10,5,2],
10)
