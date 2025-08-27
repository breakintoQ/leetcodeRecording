#改成一维矩阵，就是费空间

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        new = []
        for i in range(row):
            for j in range(column):
                new.append(matrix[i][j])
        
        length = row*column

        l = 0
        r = length-1

        if length == 1:
            if target == new[0]:
                return True    

        while l<=r:
            mid = l+(r-l)//2
            if target < new[mid]:
                r = mid-1
            elif target >new[mid]:
                l = mid+1
            else:
                return True
        return False
    

    #看题解看到的比较喜欢的解法：看是否比每行转折点小，第一次小的那一行进行二分,好像内存没小多少

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        l = 0
        r = column-1

        for i in range (row):
            if matrix[i][column-1]==target:
                return True
            elif matrix[i][column-1]>target:
                while l<=r:
                    mid = l+(r-l)//2
                    if target<matrix[i][mid]:
                        r = mid-1
                    elif target>matrix[i][mid]:
                        l = mid+1
                    else:
                        return True
                    
        return False