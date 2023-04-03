#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        
        arr = [int(x) for x in str(num)]
        max_ = max(arr)
        print(arr, max_)
        
# @lc code=end

Solution().maximumSwap(2736)