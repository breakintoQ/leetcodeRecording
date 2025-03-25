#没思路，直接看的题解

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 初始化行、列和子盒子的计数器
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        subboxes = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        
        # 遍历整个棋盘
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    index = int(c) - 1  # 将字符转换为整数索引
                    rows[i][index] += 1  # 行计数器增加
                    columns[j][index] += 1     # 列计数器增加
                    subboxes[i // 3][j // 3][index] += 1   #index表示每个盒子里的每个盒子里的1
                    # 这里如何计算盒子，相当于把盒子以3为界限划分为了三个大行和三个大列，使用//
                    
                    # 检查是否有重复的数字
                    if rows[i][index] > 1 or columns[j][index] > 1 or subboxes[i // 3][j // 3][index] > 1:
                        return False
        
        return True