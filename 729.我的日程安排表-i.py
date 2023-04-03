#
# @lc app=leetcode.cn id=729 lang=python3
#
# [729] 我的日程安排表 I
#

# @lc code=start

class TreeNode:
    def __init__(self, start, end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

# 本质就是和所有的区间比较一次，那么有序的就能快速定位
# 例如有序二分或者二分搜索树
class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
        else:
            cur = self.root
            while True:
                if start >= cur.end:
                    if not cur.right:
                        cur.right = TreeNode(start, end)
                        return True
                    cur = cur.right
                elif end <= cur.start:
                    if not cur.left:
                        cur.left = TreeNode(start, end)
                        return True
                    cur = cur.left
                else:
                    return False
        return True




# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
param_1 = obj.book(10,20)
param_1 = obj.book(5,10)
param_1 = obj.book(20,30)
# @lc code=end

