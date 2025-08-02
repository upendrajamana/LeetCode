class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j==0 or i==0:
                    matrix[i][j]=1
                else:
                    matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]
        return matrix[m-1][n-1]