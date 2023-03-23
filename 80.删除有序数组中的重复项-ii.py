#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        current = nums[0]
        count = 1
        for i in range(len(nums)):
            nums[index] = nums[i]
            index += 1
            
            if nums[i] == current:
                count += 1
                if count > 2:
                    index -= 1
            else:
                current = nums[i]
                count = 1
        return index
    
    # 着眼于满足条件的数组，[1, 1, 2, 2, 3, 4, 4, 5, 5, 9]，某个数字-2的位置一定是不同的
    # 所以可以根据这个条件来判断
    def removeDuplicates2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow = fast = 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# @lc code=end
arr = [1,1,1,2,2,3,4,4,4,4,4,4,5,5,9]
x = Solution().removeDuplicates2(arr)
print(arr)
print(x)
