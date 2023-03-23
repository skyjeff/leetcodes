#
# @lc app=leetcode.cn id=381 lang=python3
#
# [381] O(1) 时间插入、删除和获取随机元素 - 允许重复
#

# @lc code=start
from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.map = defaultdict(set)
        self.len = 0

    def insert(self, val: int) -> bool:
        
        flag = True if val not in self.map else False
        
        self.arr.append(val)
        self.map[val].add(self.len)
        self.len += 1
        return flag
        
        
    # 
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        
        del_index = self.map[val].pop()
        last = self.arr[-1]
        if len(self.map[val]) == 0:
            self.map.pop(val)
        last_index = self.len-1
        if del_index != self.len - 1:
            self.arr[del_index] = self.arr[-1]
            self.map[last].remove(last_index)
            self.map[last].add(del_index)
        self.arr.pop()
        self.len -= 1
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_2 = obj.remove(1)
param_3 = obj.getRandom()
# @lc code=end

