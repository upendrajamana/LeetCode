class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        cost_dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            cost_dp[i][0]=i
        for i in range(n+1):
            cost_dp[0][i]=i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    cost_dp[i][j]=cost_dp[i-1][j-1]
                else:
                    left=cost_dp[i][j-1]
                    top=cost_dp[i-1][j]
                    top_left=cost_dp[i-1][j-1]
                    cost_dp[i][j]=min(left,top,top_left)+1
        return cost_dp[m][n]
        


        