#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        l, r = 0, n-1
        
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            elif nums[mid] > nums[mid+1]:
                r = mid - 1
        print(mid)
        return mid        
        
# @lc code=end
Solution().findPeakElement([1,2,3,5,6,8])

