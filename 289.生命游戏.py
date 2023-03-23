#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # -1 为 1 转变为 0, 即原本为1的话，那么更新后为1，-1
        # 2 为 0 转变为 1，即原本为0的话，更新后为0， 2
        dir = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                cur = board[i][j]
                for x, y in dir:
                    dx, dy = i + x, j + y
                    if 0 <= dx < m and 0 <= dy < n and (board[dx][dy] == 1 or board[dx][dy] == -1):
                        count += 1
                if cur == 1:
                    if not (count == 2 or count == 3):
                        board[i][j] = -1
                elif cur == 0:
                    if count == 3:
                        board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    
                    board[i][j] = 0
        return board
            
# @lc code=end
x = Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
print(x)
