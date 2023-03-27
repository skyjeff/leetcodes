#
# @lc app=leetcode.cn id=611 lang=python3
#
# [611] 有效三角形的个数
#

# @lc code=start
from typing import List


class Solution:
    # 原方法是固定左边，然后双指针为i+1和n-1,原来是假如不满足，就增加left，但是这样的话right就永远是最右边的
    # 而少算最右边减少的组合比如1 4 4 5 6，永远只算了[1-5]6，而不会计算[1-4]5,[1-4]4的组合
    # 所以固定最右边，那么只需要计算r减少的方式了
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n-1, 1, -1):
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > nums[i] :
                    # print(nums[i] , nums[l] , nums[r])
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
# @lc code=end
x = Solution().triangleNumber([4,2,3,4,2,1,4])
print(x)

