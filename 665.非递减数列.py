#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
from typing import List

import sys
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        n = len(nums)
        # 两个烧饼
        nums.insert(0, -sys.maxsize)
        nums.append(sys.maxsize)
        count = 0
        for i in range(1, n):
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    return False
                
                # 考虑[3,4,2,3]有两种选择，在4这里发现递减了，有两种选择，要么改变4为2；要么是改变2为4（这里可以举例子一下看看为什么有两种选择）
                # 然后找到这里这两种选择都不能使递增的情况，即下面：
                if nums[i-1] > nums[i+1] and nums[i] > nums[i+2]:
                    return False 
        return True
                
            
# @lc code=end

