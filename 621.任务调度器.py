#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_ = [0 for _ in range(26)]
        max_ = 0
        for alpha in tasks:
            tasks_[ord(alpha) - 65] += 1
        tasks_.sort()
        # ["A","A","A","A","A","A","B", "C","D","E","F","F", "G"]
        # 出现次数最多的A为6次，那么情况为下列：
        # A B C
        # A D E 
        # A F F
        # A G X
        # A X X
        # A
        # 因为A是最多的，所以所以
        max_ = tasks_[-1]
        res = (max_ - 1) * (n + 1) 
        for i in range(26):
            if tasks_[i] == max_:
                res += 1
        # res -= 1 # 因为上面循环中会循环到max_本身对应的值
        return max(len(tasks), res)
            
        
# @lc code=end

x = Solution().leastInterval( ["A","B", "A"], 2)
print(x)