#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start


class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.indexes = {}
        
        # 关键就是伪头和伪尾
        self.head, self.tail = Node(-1), Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.len = 0
        
    def get(self, key: int) -> int:
        # get value by key
        if key in self.indexes:
            node = self.indexes[key]
            self.moveToHead(node)
            return node.value
        # if exist, move the node to the head
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        
        # 若已经在map中了
        if key in self.indexes:
            self.indexes[key].value = value  
            self.moveToHead(self.indexes[key])
        else:
            # 判断是否满
            if self.len == self.capacity:
                # 满则删除队尾，
                t = self.deleteLast()
                del self.indexes[t.key]
                self.len -= 1
                
            # 插入头
            self.putHead(node)
            # 加入到indexes中
            self.indexes[key] = node
            self.len += 1
            
    def moveToHead(self, node):
        if self.head.next != node:
            self.delete(node)
            self.putHead(node)

    def deleteLast(self):
        return self.delete(self.tail.pre)
    
    def delete(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None
        return node
        
    def putHead(self, node):
        next = self.head.next
        self.head.next = node
        node.pre = self.head
        
        node.next = next
        next.pre = node
        
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
param_1 = obj.get(2)
obj.put(1,1)

obj.put(4,1)
# @lc code=end