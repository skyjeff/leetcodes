#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 多数元素 II
#

# @lc code=start
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element1, element2 = 0, 0
        vote1, vote2 = 0, 0

        for num in nums:

            if vote1 > 0 and num == element1:
                vote1+=1
            elif vote2 > 0 and num == element2:
                vote2+=1
            elif vote1 == 0:
                element1 = num
                vote1 = 1
            elif vote2 == 0:
                element2 = num
                vote2 = 1
            else:
                vote1 -= 1
                vote2 -= 1
        res = []
        cnt1,cnt2 =0,0
        for num in nums:
            if vote1 > 0 and num == element1:
                cnt1+=1
            elif vote2 > 0 and num == element2:
                cnt2+=1
        if vote1 > 0 and cnt1 > len(nums) // 3:
            res.append(element1)
        if vote2 > 0 and cnt2 > len(nums) // 3:
            res.append(element2)

        return res
# @lc code=end

x =Solution().majorityElement([3,3,4])
print(x)