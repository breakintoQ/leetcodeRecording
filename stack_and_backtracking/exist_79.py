# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         path = []
#         used = ([False]*len(board[0]))*len(board)

#         def backtrack(row,col,index):
#             if ''.join(path) == word:
#                 return True
            
#             if path[-1]!= list(word)[index]:
#                 return 
            
#             if row!=0 and used[row-1][col]==False:
#                 path.append(board[row-1][col])
#                 used[row-1][col] = True
#                 backtrack(row-1,col,index+1)
#                 path.pop()
#                 used[row-1][col] = False

#             if col!=len(board[0])-1 and used[row][col+1]==False:
#                 path.append(board[row][col+1])
#                 used[row][col+1] = True
#                 backtrack(row,col+1,index+1)
#                 path.pop()
#                 used[row][col+1] = False
            
#             if col!=0 and used[row][col-1]==False:
#                 path.append(board[row][col-1])
#                 used[row][col-1] = True
#                 backtrack(row,col-1,index+1)
#                 path.pop()
#                 used[row][col-1] = False

#             if row!=len(board)-1 and used[row+1][col]==False:
#                 path.append(board[row+1][col])
#                 used[row+1][col] = True
#                 backtrack(row+1,col,index+1)
#                 path.pop()
#                 used[row+1][col] = False
        
#         for k in range(len(board)):
#             for s in range(len(board[0])):
#                 if board[k][s] == word[0]:
#                     path.append(board[k][s])
#                     used[k][s]=True
#                     backtrack(k,s,0)
#                     path.pop()
#                     used[k][s]=False
        
#         return False



from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        # ✔️ 问题1修正：正确初始化 used 二维数组
        used = [[False for _ in range(cols)] for _ in range(rows)]

        def backtrack(row, col, index):
            # 终止条件1：如果字符不匹配，此路不通
            if board[row][col] != word[index]:
                return False

            # 终止条件2：如果已经匹配到 word 的最后一个字符，说明找到了
            if index == len(word) - 1:
                return True

            # 标记当前位置已访问
            used[row][col] = True
            
            # 向四个方向进行探索
            # ✔️ 问题2修正：检查递归调用的返回值
            # 使用 or 连接，只要有一个方向能走通，就返回 True
            found = False
            # 上
            if row > 0 and not used[row - 1][col]:
                if backtrack(row - 1, col, index + 1):
                    found = True
            # 下
            if not found and row < rows - 1 and not used[row + 1][col]:
                if backtrack(row + 1, col, index + 1):
                    found = True
            # 左
            if not found and col > 0 and not used[row][col - 1]:
                if backtrack(row, col - 1, index + 1):
                    found = True
            # 右
            if not found and col < cols - 1 and not used[row][col + 1]:
                if backtrack(row, col + 1, index + 1):
                    found = True
            
            # 撤销选择（回溯）
            used[row][col] = False
            
            return found

        # 主循环：遍历棋盘，寻找 word 的第一个字符作为起点
        for r in range(rows):
            for c in range(cols):
                # ✔️ 问题2修正：检查 backtrack 的返回值
                if backtrack(r, c, 0):
                    return True
        
        return False