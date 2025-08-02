from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row=False
        first_col=False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i==0:
                        first_row=True
                    if j==0:
                        first_col=True

                    matrix[0][j]=0
                    matrix[i][0]=0
    # this is for setting zero to the inner matrix
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
    #setting zeros to te frist row
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if first_col:
            for j in range(len(matrix)):
                matrix[j][0]=0



        
