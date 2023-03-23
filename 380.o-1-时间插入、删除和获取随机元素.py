#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#
import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.arr = []
        self.len = 0

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = self.len
            self.arr.append(val)
            self.len += 1
            return True
        return False
            
    # 这里最便利的就是无需元素的顺序
    # 所以可以将最后一个元素填补到被删除的元素上
    # 然后修改这个最后元素的map中对应arr的索引
    # 然后arr直接pop掉这个最后的位置和删除val对应的map
    def remove(self, val: int) -> bool:
        if val in self.map:
            last = self.arr[self.len - 1]
            
            index = self.map[val]
            
            self.map[last] = index
            self.arr[index] = last
            
            self.arr.pop()
            del self.map[val]
            self.len -= 1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
param_1 = obj.insert(4)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
# @lc code=end

