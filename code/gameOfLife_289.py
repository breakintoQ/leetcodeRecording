#没看懂，给出题解
#细胞生存问题

from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        
        # 定义一个函数 count_live_neighbors 来计算某个细胞周围的活细胞数量。
        # 使用 directions 列表来表示八个方向。
        # 遍历八个方向，计算活细胞数量。
        def count_live_neighbors(r, c):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live_neighbors += 1
            return live_neighbors
        
        # 第一次遍历，标记状态变化：
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                
                if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = -1  # 活细胞变为死亡
                if board[r][c] == 0 and live_neighbors == 3:
                    board[r][c] = 2  # 死细胞变为存活
        
        # 第二次遍历，更新状态：
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0  # 更新为死亡
                if board[r][c] == 2:
                    board[r][c] = 1  # 更新为存活